from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IGPpNEqcNrK8sFkzLCRtlXeKS8Xp7pJ0PwXz3NVtZev3k9N2vQJK77sDNPawqJeJl6YT6p1qcfl3dh5MWGB5lbE00p24ZPndy',
        
    }

    return render(request, template, context)
