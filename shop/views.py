from decimal import Decimal

from django.contrib import messages
from django.db import transaction
from django.db.models import Avg
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from payments.models import Order
from .models import Product


def _get_cart(request):
    return request.session.setdefault('cart', {})


def _cart_totals(cart):
    items = []
    total = Decimal('0.00')

    for key, item in cart.items():
        line_total = Decimal(str(item['price'])) * int(item['quantity'])
        total += line_total
        items.append({
            'key': key,
            'id': item['id'],
            'title': item['title'],
            'price': Decimal(str(item['price'])),
            'quantity': item['quantity'],
            'line_total': line_total,
            'image_url': item.get('image_url', ''),
        })

    return items, total


def product_list(request):
    products = Product.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'shop/product_list.html', {'products': products})


def product_detail(request, slug=None, pk=None):
    if pk is not None:
        product = get_object_or_404(Product, pk=pk, is_active=True)
    else:
        product = get_object_or_404(Product, slug=slug, is_active=True)

    reviews = product.reviews.select_related('user').all()
    review_count = reviews.count()
    avg_rating = reviews.aggregate(avg=Avg('rating'))['avg'] or 0

    has_paid = False

    context = {
        'product': product,
        'reviews': reviews,
        'review_count': review_count,
        'avg_rating': round(avg_rating, 1),
        'has_paid': has_paid,
    }
    return render(request, 'shop/product_detail.html', context)


def cart_add(request, pk):
    product = get_object_or_404(Product, pk=pk, is_active=True)
    cart = _get_cart(request)
    product_key = str(product.id)

    if product_key in cart:
        cart[product_key]['quantity'] += 1
    else:
        cart[product_key] = {
            'id': product.id,
            'title': product.title,
            'price': str(product.price),
            'quantity': 1,
            'image_url': product.image_url or '',
        }

    request.session.modified = True
    messages.success(request, f'"{product.title}" added to cart.')
    return redirect('cart_view')


def cart_remove(request, item_key):
    cart = _get_cart(request)

    if item_key in cart:
        removed_title = cart[item_key]['title']
        del cart[item_key]
        request.session.modified = True
        messages.success(request, f'"{removed_title}" removed from cart.')

    return redirect('cart_view')


def cart_update(request, item_key):
    if request.method != 'POST':
        return redirect('cart_view')

    cart = _get_cart(request)
    if item_key not in cart:
        messages.error(request, 'Item not found in cart.')
        return redirect('cart_view')

    try:
        qty = int(request.POST.get('quantity', '1'))
    except ValueError:
        qty = 1

    if qty <= 0:
        removed_title = cart[item_key]['title']
        del cart[item_key]
        messages.success(request, f'"{removed_title}" removed from cart.')
    else:
        cart[item_key]['quantity'] = qty
        messages.success(request, f'Updated "{cart[item_key]["title"]}" to {qty}.')

    request.session.modified = True
    return redirect('cart_view')


def cart_clear(request):
    if request.method == 'POST':
        request.session['cart'] = {}
        request.session.modified = True
        messages.info(request, 'Cart cleared.')
    return redirect('cart_view')


def cart_view(request):
    cart = _get_cart(request)
    cart_items, cart_total = _cart_totals(cart)

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
        'cart_count': sum(item['quantity'] for item in cart_items),
    }
    return render(request, 'shop/cart.html', context)


@login_required
@transaction.atomic
def cart_checkout(request):
    if request.method != 'POST':
        return redirect('cart_view')

    cart = _get_cart(request)
    cart_items, cart_total = _cart_totals(cart)

    if not cart_items:
        messages.error(request, 'Your cart is empty.')
        return redirect('cart_view')

    created_orders = []

    for item in cart_items:
        product = get_object_or_404(Product, pk=item['id'], is_active=True)

        for _ in range(item['quantity']):
            order = Order.objects.create(
                user=request.user,
                product=product,
                amount=product.price,
                status='paid',
            )
            created_orders.append(order)

    request.session['cart'] = {}
    request.session.modified = True

    messages.success(request, 'Order created and marked paid (Stripe not configured).')

    if created_orders:
        return redirect('payment_success', order_id=created_orders[-1].id)

    return redirect('cart_view')
