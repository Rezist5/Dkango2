from django.shortcuts import render





def index(request):
    title = "Main"
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
    return render(request, 'index.html', context)


def about(request):
    title = "About"
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
    return render(request, 'about.html', context)


def products(request):
    title = "Catalog"
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
    return render(request, 'products.html', context)


def contact(request):
    title = "Contacts"
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
    return render(request, 'contact.html', context)


def product(request):
    title = "Product page"
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
    return render(request, 'product.html', context)
