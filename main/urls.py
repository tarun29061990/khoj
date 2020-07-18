from django.urls import path
from . import controller

urlpatterns = [
    path('query/', controller.search, name='search'),
    path('add/', controller.data_entry, name='data_entry')
]
