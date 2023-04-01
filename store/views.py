from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404


# Create your views here.
def store(request):
    all_products = Product.objects.all()
    context = {'all_products': all_products}
    return render(request, 'store/index.html', context)


def category(request):
    all_categories = Category.objects.all()
    return {'all_category': all_categories}


def list_category(request, slug=None):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)

    return render(request, 'store/list-category.html', {'category': category, 'products': products})


def product_details(request, slug):
    products = get_object_or_404(Product, slug=slug)
    context = {'product': products}
    return render(request, 'store/product-details.html', context)
