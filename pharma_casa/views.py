from django.shortcuts import render




def home(request):
    return render(request, 'home.html')


def partners(request):
    return render(request, 'Partners.html')


def contact(request):
    return render(request, 'contact.html')
