from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # Otros patrones de URL pueden ir aquí
]