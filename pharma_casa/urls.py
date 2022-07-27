from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('partners/', partners, name='partners'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
]
