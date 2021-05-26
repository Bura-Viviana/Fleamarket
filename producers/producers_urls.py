from django.urls import path

from producers.views import index, producers_list_view

app_name = 'producers'

urlpatterns = [
    path('', producers_list_view, name='index'),
]