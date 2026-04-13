from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from payments.models import Order
from services.models import CustomRequest


@login_required
def activity(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    requests = CustomRequest.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'account/activity.html', {'orders': orders, 'requests': requests})
