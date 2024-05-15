from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . views import *

urlpatterns = [

    path('productos/', lista_productos, name='productos'),
    path('productos/<int:producto_id>/', detalle_producto, name='detalle_producto'),

    #seccion administracion de productos ADMIN
    path('agregar-producto/', agregar_producto, name='agregar_producto'),
    path('listar-producto/', listar_productos, name='listar_productos'),
    path('eliminar-producto/<int:producto_id>', eliminar_producto, name='eliminar_producto'),
    path('modificar-producto/<int:producto_id>', modificar_producto, name='modificar_producto'),

    #seccion adminsitracion de marcas ADMIN
    path('listar-marcas/', listar_marcas, name='listar_marcas'),
    path('agregar-marca/', agregar_marca, name='agregar_marca'),
    path('eliminar-marca/<int:marca_id>', eliminar_marca, name='eliminar_marca'),
    path('modificar-marca/<int:marca_id>', modificar_marca, name='modificar_marca'),

    #seccion administracion de categorias ADMIN
    path('listar-categorias/', listar_categoria, name='listar_categorias'),
    path('agregar-categoria/', agregar_categoria, name='agregar_categoria'),
    path('eliminar-categoria/<int:categoria_id>', eliminar_categoria, name='eliminar_categoria'),
    path('modificar-categoria/<int:categoria_id>', modificar_categoria, name='modificar_categoria')

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
