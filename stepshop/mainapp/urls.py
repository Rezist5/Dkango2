
from django.urls import path

from mainapp.views import products, product

app_name = "products"

urlpatterns = [
    path('', products, name="index"),
    path('product/', product, name="product"),
    path('products/', product, name="products"),
    path('contact/', product, name="contact"),
    path('about/', product, name="about"),
]
