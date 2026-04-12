from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from services.models import CustomRequest
from shop.models import Product

from .forms import ReviewForm
from .models import Review


def _redirect_target(review):
    if review.product:
        return reverse('product_detail', args=[review.product.slug])
    if review.custom_request:
        return reverse('request_detail', args=[review.custom_request.pk])
    return '/'


@login_required
def create_product_review(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    existing = Review.objects.filter(user=request.user, product=product).first()
    if existing:
        messages.info(request, 'You already reviewed this product. You can edit it instead.')
        return redirect('edit_review', pk=existing.pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            messages.success(request, 'Thanks for your review!')
            return redirect('product_detail', slug=product.slug)
    else:
        form = ReviewForm()

    return render(request, 'reviews/review_form.html', {
        'form': form,
        'target': product,
        'title': f'Review {product.title}',
    })


@login_required
def create_request_review(request, pk):
    custom_request = get_object_or_404(CustomRequest, pk=pk, user=request.user)
    existing = Review.objects.filter(user=request.user, custom_request=custom_request).first()
    if existing:
        messages.info(request, 'You already reviewed this request. You can edit it instead.')
        return redirect('edit_review', pk=existing.pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.custom_request = custom_request
            review.save()
            messages.success(request, 'Thanks for your review!')
            return redirect('request_detail', pk=custom_request.pk)
    else:
        form = ReviewForm()

    return render(request, 'reviews/review_form.html', {
        'form': form,
        'target': custom_request,
        'title': f'Review request #{custom_request.pk}',
    })


@login_required
def edit_review(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review updated.')
            return redirect(_redirect_target(review))
    else:
        form = ReviewForm(instance=review)

    return render(request, 'reviews/review_form.html', {
        'form': form,
        'target': review.product or review.custom_request,
        'title': 'Edit review',
    })


@login_required
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    target_url = _redirect_target(review)
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Review deleted.')
        return redirect(target_url)

    return render(request, 'reviews/review_confirm_delete.html', {'review': review})
