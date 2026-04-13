from decimal import Decimal

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.urls import reverse

from shop.models import Product

from .models import Order, Payment

try:
    import stripe
    if getattr(settings, 'STRIPE_SECRET_KEY', None):
        stripe.api_key = settings.STRIPE_SECRET_KEY
    else:
        stripe = None
except ImportError:  # pragma: no cover - if stripe not installed we fallback
    stripe = None


def _retrieve_session(session_id: str):
    """Safely retrieve a Stripe Checkout Session with expanded payment intent."""
    if not session_id or stripe is None or not getattr(stripe, 'api_key', None):
        return None
    try:
        return stripe.checkout.Session.retrieve(
            session_id,
            expand=['payment_intent'],
        )
    except Exception:
        return None


@login_required
def buy_now(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)

    if request.method != 'POST':
        return redirect('product_detail', slug=slug)

    order = Order.objects.create(
        user=request.user,
        product=product,
        price_snapshot=Decimal(product.price),
        status='pending',
    )
    if stripe is None or not getattr(stripe, 'api_key', None):
        order.status = 'paid'
        order.save(update_fields=['status'])
        Payment.objects.create(
            user=request.user,
            order=order,
            amount=order.price_snapshot,
            status='succeeded',
            paid_at=timezone.now(),
        )
        messages.success(request, 'Order created and marked paid (Stripe not configured).')
        return redirect('order_detail', pk=order.pk)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        mode='payment',
        line_items=[{
            'price_data': {
                'currency': 'eur',
                'product_data': {'name': product.title},
                'unit_amount': int(order.price_snapshot * 100),
            },
            'quantity': 1,
        }],
        success_url=request.build_absolute_uri(reverse('order_success', args=[order.pk])) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('order_cancel', args=[order.pk])),
    )
    order.stripe_session_id = session.id
    order.save(update_fields=['stripe_session_id'])
    Payment.objects.create(
        user=request.user,
        order=order,
        amount=order.price_snapshot,
        status='pending',
        stripe_session_id=session.id,
    )
    return redirect(session.url)


@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    paid_flag = request.GET.get('paid')
    if paid_flag and order.status != 'paid':
        order.status = 'paid'
        order.save(update_fields=['status'])
        Payment.objects.filter(order=order).update(status='succeeded', paid_at=timezone.now())
    return render(request, 'payments/order_detail.html', {'order': order})


@login_required
def order_success(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    payment = Payment.objects.filter(order=order).order_by('-created_at').first()
    session_id = request.GET.get('session_id') or order.stripe_session_id or (payment.stripe_session_id if payment else None)
    session = _retrieve_session(session_id)

    if session and session.payment_status == 'paid':
        order.status = 'paid'
        order.stripe_session_id = session.id
        order.save(update_fields=['status', 'stripe_session_id'])

        payment, _ = Payment.objects.get_or_create(
            order=order,
            defaults={
                'user': request.user,
                'amount': order.price_snapshot,
                'status': 'pending',
                'stripe_session_id': session.id,
            },
        )
        payment.status = 'succeeded'
        payment.paid_at = timezone.now()
        payment.stripe_session_id = session.id
        payment.stripe_payment_intent = getattr(session, 'payment_intent', '') or ''
        payment.save()
    elif order.status != 'paid':
        messages.error(request, 'We could not confirm the Stripe payment. Please try again or contact support.')

    return render(request, 'payments/order_success.html', {'order': order})


@login_required
def order_cancel(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    order.status = 'cancelled'
    order.save(update_fields=['status'])
    Payment.objects.filter(order=order, status='pending').update(status='failed')
    messages.info(request, 'Payment cancelled.')
    return render(request, 'payments/order_cancel.html', {'order': order})


@login_required
def request_checkout(request, pk):
    from services.models import CustomRequest
    custom_request = get_object_or_404(CustomRequest, pk=pk, user=request.user)

    if request.method != 'POST':
        return redirect('request_detail', pk=pk)

    amount = Decimal(custom_request.total_price)

    if stripe is None or not getattr(stripe, 'api_key', None):
        Payment.objects.create(
            user=request.user,
            custom_request=custom_request,
            amount=amount,
            status='succeeded',
            paid_at=timezone.now(),
        )
        custom_request.status = 'completed'
        custom_request.save(update_fields=['status'])
        messages.success(request, 'Marked paid (Stripe not configured).')
        return redirect('request_checkout_success', pk=custom_request.pk)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        mode='payment',
        line_items=[{
            'price_data': {
                'currency': 'eur',
                'product_data': {'name': f'Custom request #{custom_request.pk}'},
                'unit_amount': int(amount * 100),
            },
            'quantity': 1,
        }],
        success_url=request.build_absolute_uri(reverse('request_checkout_success', args=[custom_request.pk])) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('request_checkout_cancel', args=[custom_request.pk])),
    )
    Payment.objects.create(
        user=request.user,
        custom_request=custom_request,
        amount=amount,
        status='pending',
        stripe_session_id=session.id,
    )
    return redirect(session.url)


@login_required
def request_checkout_success(request, pk):
    from services.models import CustomRequest
    custom_request = get_object_or_404(CustomRequest, pk=pk, user=request.user)
    payment = Payment.objects.filter(custom_request=custom_request).order_by('-created_at').first()
    session_id = request.GET.get('session_id') or (payment.stripe_session_id if payment else None)
    session = _retrieve_session(session_id)

    if session and session.payment_status == 'paid':
        custom_request.status = 'completed'
        custom_request.save(update_fields=['status'])
        payment, _ = Payment.objects.get_or_create(
            custom_request=custom_request,
            defaults={
                'user': request.user,
                'amount': custom_request.total_price,
                'status': 'pending',
                'stripe_session_id': session.id,
            },
        )
        payment.status = 'succeeded'
        payment.paid_at = timezone.now()
        payment.stripe_session_id = session.id
        payment.stripe_payment_intent = getattr(session, 'payment_intent', '') or ''
        payment.save()
    elif custom_request.status != 'completed':
        messages.error(request, 'We could not confirm the Stripe payment. Please try again or contact support.')

    return render(request, 'payments/request_success.html', {'custom_request': custom_request})


@login_required
def request_checkout_cancel(request, pk):
    from services.models import CustomRequest
    custom_request = get_object_or_404(CustomRequest, pk=pk, user=request.user)
    custom_request.status = 'cancelled'
    custom_request.save(update_fields=['status'])
    Payment.objects.filter(custom_request=custom_request, status='pending').update(status='failed')
    messages.info(request, 'Payment cancelled.')
    return render(request, 'payments/request_cancel.html', {'custom_request': custom_request})
