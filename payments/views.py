from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from shop.models import Product

from .models import Order


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
    messages.success(request, 'Order created. Payment step coming soon.')
    return redirect('order_detail', pk=order.pk)


@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, 'payments/order_detail.html', {'order': order})
