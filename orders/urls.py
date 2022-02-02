from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', csrf_exempt(views.order), name = 'order'),
    path('create-order',csrf_exempt(views.create_order), name = 'create-order'),
    path('edit-order/<int:id>',views.edit_order, name='edit-order'),
    path('delete-order/<int:id>',views.delete_order, name='delete-order'),
    path('search-order', csrf_exempt(views.search_order), name='search-order')
]