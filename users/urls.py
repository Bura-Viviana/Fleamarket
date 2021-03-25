from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('login/', auth_views.LoginView.as_view(teampleate_name='login.html')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html')),
    path('', include('django.contrib.auth.urls')),
]
