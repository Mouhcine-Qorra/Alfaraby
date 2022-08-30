from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('homeA/', homeA, name='homeA'),
    path('exemple/', exemple, name='exemple'),
    path('products/', products, name='products'),
    path('pdf/', show_pdf, name='pdf'),
    path('partners/', partners, name='partners'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('about/', about, name='about'),
]
