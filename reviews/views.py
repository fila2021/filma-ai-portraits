from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from shop.models import Product
from services.models import CustomRequest

from .models import Review
from .forms import ReviewForm


def review_list(request):
    """
    Display all reviews (latest first)
    """
    reviews = Review.objects.select_related(
        'user',
        'product',
        'custom_request'
    ).all()

    context = {
        'reviews': reviews
    }
    return render(request, 'reviews/review_list.html', context)


@login_required
def add_product_review(request, product_id):
    """
    Add a review for a specific product
    """
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return redirect('product_detail_by_id', pk=product.id)
    else:
        form = ReviewForm()

    context = {
        'form': form,
        'target': product,
        'type': 'product'
    }
    return render(request, 'reviews/add_review.html', context)


@login_required
def add_custom_request_review(request, request_id):
    """
    Add a review for a custom request
    """
    custom_request = get_object_or_404(CustomRequest, id=request_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.custom_request = custom_request
            review.save()
            return redirect('request_detail', pk=custom_request.id)
    else:
        form = ReviewForm()

    context = {
        'form': form,
        'target': custom_request,
        'type': 'custom_request'
    }
    return render(request, 'reviews/add_review.html', context)
