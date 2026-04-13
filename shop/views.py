from decimal import Decimal

from django.contrib import messages
from django.db.models import Avg
from django.shortcuts import get_object_or_404, redirect, render

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


def cart_view(request):
    cart = _get_cart(request)
    cart_items, cart_total = _cart_totals(cart)

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
        'cart_count': sum(item['quantity'] for item in cart_items),
    }
    return render(request, 'shop/cart.html', context)