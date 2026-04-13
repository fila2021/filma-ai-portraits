from django.shortcuts import render


def home(request):
    return render(request, 'home/index.html')


def browse(request):
    from shop.models import Product
    from services.models import ServicePackage

    products = Product.objects.filter(is_active=True).order_by('-created_at')
    services = ServicePackage.objects.filter(is_active=True).order_by('name')

    return render(
        request,
        'home/browse.html',
        {
            'products': products,
            'services': services,
        }
    )
