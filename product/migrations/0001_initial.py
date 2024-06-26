# Generated by Django 5.0.6 on 2024-05-11 23:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_marca', models.CharField(help_text='Ingresa el nombre de la marca del producto', max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(default='Producto', help_text='Ingrese el nombre del producto', max_length=100)),
                ('descripcion_producto', models.TextField(help_text='Ingrese la descripcion del producto', max_length=1000)),
                ('stock_producto', models.IntegerField(default=1, help_text='Ingrese el stock del producto')),
                ('precio_producto', models.IntegerField(default=1, help_text='Ingrese el precio del producto')),
                ('descripcion_tecnica', models.TextField(help_text='Ingrese la descripcion tecnica', max_length=1000)),
                ('img_producto', models.ImageField(default='https://static.thenounproject.com/png/2535689-200.png', help_text='Ingrese imagenes del producto', upload_to='fotosProductos')),
                ('marca_producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='product.marca')),
                ('nombre_categoria', models.ManyToManyField(to='product.categoria')),
            ],
        ),
    ]
