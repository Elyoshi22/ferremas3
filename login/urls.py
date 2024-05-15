from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('header/', views.header, name='header'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Otros patrones de URL pueden ir aquí
]