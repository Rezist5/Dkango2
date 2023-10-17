from django.shortcuts import render


def links_m(title):
    links_menu = [
        {'link': 'index', 'name': "Главная"},
        {'link': 'products:index', 'name': "Продукты"},
        {'link': 'about', 'name': "О нас"},
        {'link': 'contact', 'name': "Контакты"},
    ]
    context = {
        'title': title,
        'links_menu': links_menu,
    }
    return context


def index(request):
    title = "Main"
    return render(request, 'index.html', links_m(title))


def about(request):
    title = "About"
    return render(request, 'about.html', links_m(title))


def products(request):
    title = "Catalog"
    return render(request, 'products.html', links_m(title))


def contact(request):
    title = "Contacts"
    return render(request, 'contact.html', links_m(title))


def product(request):
    title = "Product page"
    return render(request, 'product.html', links_m(title))
