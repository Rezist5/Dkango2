from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, Category


def links_m(**kwargs):
    links_menu = [
        {'link': 'index', 'name': "Главная"},
        {'link': 'products:index', 'name': "Продукты"},
        {'link': 'about', 'name': "О нас"},
        {'link': 'contact', 'name': "Контакты"},
    ]
    categories = Category.objects.all()

    context = {
        'links_menu': links_menu,
        'categories': categories,
    }
    context.update(**kwargs)
    return context


def get_basket(user):
    if user.is_authenticated:
        return  Basket.objects.filter(user=user)
    return []

def index(request):
    title = "Main"
    prods = Product.objects.all()
    context = links_m(title=title, prods=prods)
    return render(request, 'index.html', context)


def about(request):
    title = "About"
    context = links_m(title=title)
    return render(request, 'about.html', context)


def products(request, pk=None):
    title = "Catalog"
    # prods = Product.objects.all()
    prods = Product.objects.order_by('price')
    context = {}
    basket = get_basket(request.user)

    if pk is not None:
        category = get_object_or_404(Category, pk=pk)
        prods = Product.objects.filter(category__pk=pk).order_by('price')
        context = links_m(category=category)

    context = links_m(title=title, prods=prods, basket=basket, **context)
    return render(request, 'products.html', context)


def contact(request):
    title = "Contacts"
    context = links_m(title=title)
    return render(request, 'contact.html', context)


def product(request, pk):
    title = "Product page"
    prod = Product.objects.get(pk=pk)
    same_prods = Product.objects.exclude(pk=pk)#.filter(category=prod.category)
    context = links_m(title=title, prod=prod, same_prods=same_prods)
    return render(request, 'product.html', context)
