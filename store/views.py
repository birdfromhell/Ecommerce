from django.shortcuts import render
from .models import Category


# Create your views here.
def store(request):
    return render(request, 'store/index.html')


def category(request):
    categories = Category.objects.all()
    return {'category': categories}
