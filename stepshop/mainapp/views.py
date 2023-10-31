from django.shortcuts import render

from mainapp.models import Product


def links_m(**kwargs):
    links_menu = [
        {'link': 'index', 'name': "Главная"},
        {'link': 'products:index', 'name': "Продукты"},
        {'link': 'about', 'name': "О нас"},
        {'link': 'contact', 'name': "Контакты"},
    ]
    context = {
        'links_menu': links_menu,
    }
    context.update(**kwargs)
    return context


def index(request):
    title = "Main"
    prods = Product.objects.all()
    context = links_m(title=title, prods=prods)
    return render(request, 'index.html', context)


def about(request):
    title = "About"
    context = links_m(title=title)
    return render(request, 'about.html', context)


def products(request):
    title = "Catalog"
    prods = Product.objects.all()
    context = links_m(title=title, prods=prods)
    return render(request, 'products.html', context)


def contact(request):
    title = "Contacts"
    context = links_m(title=title)
    return render(request, 'contact.html', context)


def product(request, pk):
    title = "Product page"
    prod = Product.objects.get(pk=pk)
    context = links_m(title=title, prod=prod)
    return render(request, 'product.html', context)
