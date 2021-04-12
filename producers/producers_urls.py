from django.urls import path

from producers.views import index

urlpatterns = [
    path('', index, name='index'),
]