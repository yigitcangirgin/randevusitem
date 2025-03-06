from django.urls import path 
from . import views
urlpatterns = [
    path('' , views.index , name='pages_index'),
    path('about/' , views.about , name='about'),
    path('rezervation/' , views.rezervation , name='rezervation'),
    path('contact/' , views.contact , name='contact'),
]