from django.urls import path
from . import controller

urlpatterns = [
    path('main', controller.index, name='index'),
    path('', controller.index,name='index'),
    path('query/', controller.search, name='search'),
    path('add/', controller.data_entry, name='data_entry')
]
