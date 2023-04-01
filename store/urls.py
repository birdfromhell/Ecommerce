from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('products/<slug:slug>', views.product_details, name='product-detail'),
    path('category/<slug:slug>', views.list_category,name='list-category'),

]
