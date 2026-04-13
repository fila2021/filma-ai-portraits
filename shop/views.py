from django.shortcuts import get_object_or_404, render
from django.db.models import Avg
from .models import Product


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

    # Keep this simple for now unless you later connect real paid-order logic
    has_paid = False

    context = {
        'product': product,
        'reviews': reviews,
        'review_count': review_count,
        'avg_rating': round(avg_rating, 1),
        'has_paid': has_paid,
    }
    return render(request, 'shop/product_detail.html', context)