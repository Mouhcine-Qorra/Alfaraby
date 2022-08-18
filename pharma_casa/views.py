from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from .sendEmail import sendEmail
import os



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
    if request.method == "POST" :
        sendEmail(Name=request.POST['Name'], Email=request.POST['Email'], Message=request.POST['Message'])
    return render(request, 'contact.html')


def blog(request):
    return render(request, 'Blog.html')


def about(request):
    return render(request, 'about.html')


def show_pdf(request):
    filepath = os.path.join('static', 'products.pdf')
    # fsock = open(filepath, "rb")
    # response = HttpResponse(fsock, content_type='application/pdf')
    # response['Content-Disposition'] = 'inline; filename=products.pdf'
    #return response
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')   # from django.http import FileResponse     for viewing only

