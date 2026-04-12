from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import CustomRequest, ServicePackage


class CreateRequestViewTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="alice",
            email="alice@example.com",
            password="testpass123",
        )
        self.package = ServicePackage.objects.create(
            name="Starter Social Set",
            description="10 portraits for IG/TikTok",
            base_price=Decimal("39.00"),
            number_of_images=10,
            turnaround_days=2,
            platform_type="instagram",
        )

    def test_create_request_happy_path(self):
        self.client.login(username="alice", password="testpass123")

        response = self.client.post(
            reverse("create_request"),
            {
                "package": self.package.id,
                "platform_type": "instagram",
                "style_choice": "realistic",
                "prompt_details": "Cinematic headshot, golden hour, shallow depth of field.",
                "extra_notes": "Deliver in square crop.",
            },
            follow=False,
        )

        # Should redirect to success page
        self.assertEqual(response.status_code, 302)
        self.assertIn("/services/requests/", response["Location"])
        self.assertIn("/success/", response["Location"])

        created = CustomRequest.objects.get()
        self.assertEqual(created.user, self.user)
        self.assertEqual(created.package, self.package)
        self.assertEqual(created.total_price, self.package.base_price)
        self.assertEqual(created.status, "pending")


class RequestCrudFlowTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="bob",
            email="bob@example.com",
            password="testpass123",
        )
        self.other = User.objects.create_user(
            username="charlie",
            email="charlie@example.com",
            password="testpass123",
        )
        self.package = ServicePackage.objects.create(
            name="Creator Growth",
            description="25 images for socials",
            base_price=Decimal("79.00"),
            number_of_images=25,
            turnaround_days=3,
            platform_type="facebook",
        )

    def _create_request(self, user=None, **kwargs):
        return CustomRequest.objects.create(
            user=user or self.user,
            package=self.package,
            platform_type="facebook",
            style_choice="cartoon",
            prompt_details="Cartoon avatar with bold colors and thick outlines.",
            extra_notes="",
            total_price=self.package.base_price,
            **kwargs,
        )

    def test_request_list_requires_login(self):
        response = self.client.get(reverse("request_list"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response["Location"])

    def test_request_list_shows_only_user_items(self):
        mine = self._create_request()
        theirs = self._create_request(user=self.other)

        self.client.login(username="bob", password="testpass123")
        response = self.client.get(reverse("request_list"))

        requests = response.context["requests"]
        self.assertEqual(list(requests), [mine])

    def test_request_detail_requires_owner(self):
        req = self._create_request(user=self.other)
        self.client.login(username="bob", password="testpass123")
        response = self.client.get(reverse("request_detail", args=[req.pk]))
        self.assertEqual(response.status_code, 404)

    def test_edit_request_updates_prompt_and_price(self):
        req = self._create_request()
        self.client.login(username="bob", password="testpass123")

        response = self.client.post(
            reverse("edit_request", args=[req.pk]),
            {
                "package": self.package.id,
                "platform_type": "facebook",
                "style_choice": "cinematic",
                "prompt_details": "Cinematic portrait with dramatic lighting.",
                "extra_notes": "Please add teal/orange grade.",
            },
            follow=False,
        )

        self.assertEqual(response.status_code, 302)
        req.refresh_from_db()
        self.assertEqual(req.style_choice, "cinematic")
        self.assertEqual(req.total_price, self.package.base_price)

    def test_edit_request_blocks_non_pending(self):
        req = self._create_request(status="completed")
        self.client.login(username="bob", password="testpass123")
        response = self.client.post(
            reverse("edit_request", args=[req.pk]),
            {
                "package": self.package.id,
                "platform_type": "facebook",
                "style_choice": "cinematic",
                "prompt_details": "Cinematic portrait with dramatic lighting.",
                "extra_notes": "",
            },
            follow=False,
        )
        self.assertEqual(response.status_code, 302)
        messages = list(response.wsgi_request._messages)
        self.assertTrue(any("Only pending requests can be edited." in str(m) for m in messages))

    def test_delete_request(self):
        req = self._create_request()
        self.client.login(username="bob", password="testpass123")

        response = self.client.post(reverse("delete_request", args=[req.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(CustomRequest.objects.filter(pk=req.pk).exists())
