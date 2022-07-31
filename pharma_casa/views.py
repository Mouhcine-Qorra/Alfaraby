from django.shortcuts import render




def home(request):
    return render(request, 'home.html')
def homeA(request):
    return render(request, 'homeA.html')
def exemple(request):
    return render(request, 'exemple.html')


def products(request):
    return render(request, 'products.html')


def partners(request):
    return render(request, 'Partners.html')


def contact(request):
    return render(request, 'contact.html')


def blog(request):
    return render(request, 'Blog.html')


def about(request):
    return render(request, 'about.html')
