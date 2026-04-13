from django.core.paginator import Paginator
from django.shortcuts import render

from .models import PromptBundle, PromptSample


def home(request):
    # Show a few recent portrait products on the homepage
    from shop.models import Product

    featured_products = Product.objects.filter(is_active=True).order_by('-created_at')[:3]
    return render(request, 'home/index.html', {
        'featured_products': featured_products,
    })


def browse(request):
    from shop.models import Product
    from services.models import ServicePackage

    products = Product.objects.filter(is_active=True).order_by('-created_at')
    products_page = Paginator(products, 8).get_page(request.GET.get('p'))
    services = ServicePackage.objects.filter(is_active=True).order_by('name')

    return render(
        request,
        'home/browse.html',
        {
            'products_page': products_page,
            'services': services,
        }
    )


def ai_photos(request):
    from shop.models import Product
    products = Product.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'home/ai_photos.html', {'products': products})


def ai_bundles(request):
    bundles = PromptBundle.objects.all()
    bundles_page = Paginator(bundles, 9).get_page(request.GET.get('page'))
    sample_prompts = PromptSample.objects.all()
    return render(request, 'home/bundles.html', {
        'prompts': sample_prompts,
        'bundles_page': bundles_page,
    })
