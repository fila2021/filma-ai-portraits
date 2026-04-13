from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CustomRequestForm
from .models import CustomRequest, ServicePackage


def service_list(request):
    services = ServicePackage.objects.filter(is_active=True)
    return render(request, 'services/service_list.html', {'services': services})


def service_detail(request, pk):
    service = get_object_or_404(ServicePackage, pk=pk, is_active=True)
    return render(request, 'services/service_detail.html', {'service': service})


@login_required
def request_list(request):
    requests = CustomRequest.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'services/request_list.html', {'requests': requests})


@login_required
def request_detail(request, pk):
    custom_request = get_object_or_404(CustomRequest, pk=pk, user=request.user)
    return render(request, 'services/request_detail.html', {'custom_request': custom_request})


@login_required
def create_request(request):
    if request.method == 'POST':
        form = CustomRequestForm(request.POST)
        if form.is_valid():
            custom_request = form.save(commit=False)
            custom_request.user = request.user
            custom_request.total_price = Decimal(custom_request.package.base_price)
            custom_request.save()
            messages.success(request, 'Your custom request has been created successfully.')
            return redirect('request_success', pk=custom_request.pk)
    else:
        form = CustomRequestForm()

    return render(request, 'services/create_request.html', {'form': form})


@login_required
def edit_request(request, pk):
    custom_request = get_object_or_404(CustomRequest, pk=pk, user=request.user)

    if custom_request.status != 'pending':
        messages.error(request, 'Only pending requests can be edited.')
        return redirect('request_detail', pk=custom_request.pk)

    if request.method == 'POST':
        form = CustomRequestForm(request.POST, instance=custom_request)
        if form.is_valid():
            updated_request = form.save(commit=False)
            updated_request.total_price = Decimal(updated_request.package.base_price)
            updated_request.save()
            messages.success(request, 'Your custom request was updated successfully.')
            return redirect('request_detail', pk=updated_request.pk)
    else:
        form = CustomRequestForm(instance=custom_request)

    return render(
        request,
        'services/edit_request.html',
        {'form': form, 'custom_request': custom_request}
    )


@login_required
def request_success(request, pk):
    custom_request = get_object_or_404(CustomRequest, pk=pk, user=request.user)
    return render(request, 'services/request_success.html', {'custom_request': custom_request})


@login_required
def delete_request(request, pk):
    custom_request = get_object_or_404(CustomRequest, pk=pk, user=request.user)

    if request.method == 'POST':
        custom_request.delete()
        messages.success(request, 'Your custom request was deleted successfully.')
        return redirect('request_list')

    return render(
        request,
        'services/delete_request.html',
        {'custom_request': custom_request}
    )
