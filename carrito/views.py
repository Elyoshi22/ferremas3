from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from product.models import Producto
from .models import Carrito, ItemCarrito
import mercadopago
from django.conf import settings

@login_required
def carrito(request):
    try:
        carrito = Carrito.objects.get(usuario=request.user)
        items_carrito = ItemCarrito.objects.filter(carrito=carrito)
        
        items = []
        for item in items_carrito:
            items.append({
                "title": item.producto.nombre_producto,
                "quantity": item.cantidad,
                "currency_id": "CLP",
                "unit_price": float(item.producto.precio_producto)
            })

        sdk = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_TOKEN)

        preference_data = {
            "items": items,
            "back_urls": {
                "success": request.build_absolute_uri('/pago_exitoso/'),
                "failure": request.build_absolute_uri('/pago_fallido/'),
                "pending": request.build_absolute_uri('/pago_pendiente/')
            },
            "auto_return": "approved",
            "site_id": "MLC"  # Asegúrate de que este site_id sea correcto para Chile
        }

        preference_response = sdk.preference().create(preference_data)
        preference = preference_response["response"]

    except Carrito.DoesNotExist:
        carrito = None
        items_carrito = []
        preference = None

    return render(request, 'carrito.html', {
        'carrito': carrito,
        'items': items_carrito,
        'preference': preference,
        'public_key': settings.MERCADOPAGO_PUBLIC_KEY
    })

def actualizar_carrito(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('cantidad_'):
                item_id = key.split('_')[1]
                try:
                    item = ItemCarrito.objects.get(id=item_id)
                    item.cantidad = int(value)
                    item.save()
                except ItemCarrito.DoesNotExist:
                    pass
    return redirect('carrito')

# Otros métodos para el proceso de pago
def procesar_pago(request):
    if request.method == 'POST':
        carrito = Carrito.objects.get(usuario=request.user)
        items_carrito = ItemCarrito.objects.filter(carrito=carrito)

        items = []
        for item in items_carrito:
            items.append({
                "title": item.producto.nombre_producto,
                "quantity": item.cantidad,
                "currency_id": "CLP",
                "unit_price": float(item.producto.precio_producto)
            })

        sdk = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_TOKEN)

        preference_data = {
            "items": items,
            "back_urls": {
                "success": request.build_absolute_uri('/pago_exitoso/'),
                "failure": request.build_absolute_uri('/pago_fallido/'),
                "pending": request.build_absolute_uri('/pago_pendiente/')
            },
            "auto_return": "approved",
            "site_id": "MLC"
        }

        preference_response = sdk.preference().create(preference_data)
        preference = preference_response["response"]

        return redirect(preference['init_point'])

    return render(request, 'procesar_pago.html')

def pago_exitoso(request):
    return render(request, 'pago_exitoso.html')

def pago_fallido(request):
    return render(request, 'pago_fallido.html')

def pago_pendiente(request):
    return render(request, 'pago_pendiente.html')
