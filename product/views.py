from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Marca, Categoria
from django.views import generic
from .forms import ProductoForm, MarcaForm, CategoriaForm
from django.contrib import messages
import requests #pip install requests

#obtener divisa
def obtener_tasas_de_cambio():
    api_key = 'fed961042f58b1c4296609fa135d6c24'
    url = f'http://data.fixer.io/api/latest?access_key={api_key}&symbols=USD,EUR'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data['rates']
    else:
        return None

def lista_productos(request):
    productos = Producto.objects.all()
    divisa = request.GET.get('divisa', 'CLP')  
    tasas_de_cambio = obtener_tasas_de_cambio()
    
    for producto in productos:
        if divisa != 'CLP':
            if divisa == 'USD':
                producto.precio_producto_usd = round(producto.precio_producto / tasas_de_cambio['USD'], 2)
            elif divisa == 'EUR':
                producto.precio_producto_eur = round(producto.precio_producto / tasas_de_cambio['EUR'], 2)
    
    return render(request, 'productos.html', {'productos': productos, 'divisa': divisa})

def show_products(request):
    producto_list = Producto.objects.all()
    return render (request, 'productos.html', {'producto_list': producto_list})


#Detalle de los productos
def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})


#
#seccion manejo de productos ADMIN
#

#Agrega productos desde la pagina seccion ADMIN
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'form_product.html', {'form':form})



#Muestra los productos seccion ADMIN
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_producto.html', {'productos': productos})


#Elimina el producto de la BD seccion ADMIN
def eliminar_producto(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'El producto ha sido eliminado exitosamente.')
        return redirect('listar_productos')
    return render(request, 'lista_producto.html', {'producto': producto})



#modificar datos de productos ADMIN
def modificar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'modificar_producto.html', {'form':form})



#
#seccion manejo de marcas ADMIN
#

#Agregar marca desde la pagina seccion ADMIN
def agregar_marca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_marcas')
    else:
        form = MarcaForm()
    return render(request, 'form_marca.html', {'form':form})


#Muestra las marcas seccion ADMIN
def listar_marcas(request):
    marcas = Marca.objects.all()
    return render(request, 'listar_marcas.html', {'marcas':marcas})


#Eliminar la marca de la BD seccion ADMIN
def eliminar_marca(request, marca_id):
    marca = Marca.objects.get(pk=marca_id)
    if request.method == 'POST':
        marca.delete()
        messages.success(request, 'La marca ha sido eliminada exitosamente.')
        return redirect('listar_marcas')
    return render(request, 'listar_marcas.html', {'marca':marca})

#modificar datos de marcas ADMIN
def modificar_marca(request, marca_id):
    marca = get_object_or_404(Marca, pk=marca_id)
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('listar_marcas')
    else:
        form = MarcaForm(instance=marca)
    return render(request, 'modificar_marca.html', {'form': form})




#
#seccion manejo de categoria ADMIN
#

#Agregar categoria desde la pagina seccion ADMIN
def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
        return render(request, 'form_categoria.html', {'form':form})


#Muerstra las categorias seccion ADMIN
def listar_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'listar_categoria.html', {'categorias':categorias})

#Eliminar la categorias de la BD seccion ADMIN
def eliminar_categoria(request, categoria_id):
    categoria = Categoria.objects.get(pk=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'La categoria ha sido eliminada exitosamente.')
        return redirect('listar_categorias')
    return render(request, 'lisar_categoria.html', {'categoria':categoria})

#Modificar datos de categorias ADMIN
def modificar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'modificar_categoria.html', {'form':form})