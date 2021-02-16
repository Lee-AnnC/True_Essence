from django.views.generic import ListView, DetailView
from . models import blog


class blogListView(ListView):
    model = blog
    template_name = 'home.html'


class blogDetailView(DetailView):
    model = blog
    template_name = 'detail.html'
