from django.urls import path

from producers.views import index, producers_list_view
from producers.views import index, products_list_view

app_name = 'producers'

urlpatterns = [
    path('', producers_list_view, name='index'),
    path('products', products_list_view, name='products'),
]