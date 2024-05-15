from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_categoria


class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_marca = models.CharField(max_length=50, help_text="Ingresa el nombre de la marca del producto", unique=True)

    def __str__(self):
        return self.nombre_marca
    
    

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    marca_producto = models.ForeignKey('Marca', on_delete=models.RESTRICT, null=True)
    nombre_producto = models.CharField(max_length=100, default="Producto" , help_text="Ingrese el nombre del producto")
    descripcion_producto = models.TextField(max_length=2000, help_text="Ingrese la descripcion del producto")
    stock_producto = models.IntegerField(help_text="Ingrese el stock del producto", default=1)
    precio_producto = models.FloatField(default=1, help_text="Ingrese el precio del producto")
    descripcion_tecnica = models.TextField(max_length=2000, help_text="Ingrese la descripcion tecnica")
    img_producto = models.ImageField(upload_to="fotosProductos", default="https://static.thenounproject.com/png/2535689-200.png", help_text="Ingrese imagenes del producto")
    nombre_categoria = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.nombre_producto
    

