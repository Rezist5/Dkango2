from django.urls import path

from mainapp.views import products, product

urlpatterns = [
    path('', products, name="index"),
    path('product/', product, name="product"),
]