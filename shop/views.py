from django.shortcuts import render

# Create your views here.


def shop(request):
    """ A view to return the online shop page """

    return render(request, 'shop/shop.html')
