from django import forms
from .models import Producto, Marca, Categoria

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['marca_producto', 'nombre_producto', 'descripcion_producto', 'stock_producto', 'descripcion_tecnica', 'img_producto', 'nombre_categoria']


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre_marca']


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre_categoria']