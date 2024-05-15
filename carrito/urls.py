from django.urls import path
from . import views

urlpatterns = [
    path('', views.carrito, name='carrito'),
    
    path('actualizar/', views.actualizar_carrito, name='actualizar_carrito'),
    path('procesar_pago/', views.procesar_pago, name='procesar_pago'),
    path('pago_exitoso/', views.pago_exitoso, name='pago_exitoso'),
    path('pago_fallido/', views.pago_fallido, name='pago_fallido'),
    path('pago_pendiente/', views.pago_pendiente, name='pago_pendiente'),
]