from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def http404(request, exception):
    return render(request, 'home/404.html')


def http500(request):
    return render(request, 'home/500.html')
