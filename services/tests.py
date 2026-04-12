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
