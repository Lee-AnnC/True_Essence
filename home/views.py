from django.shortcuts import render
from . import views

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def http404(request, exception):
    return render(request, views.http404)


def http500(request):
    return render(request, views.http500)
