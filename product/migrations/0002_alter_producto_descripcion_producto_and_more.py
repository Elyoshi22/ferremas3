# Generated by Django 5.0.6 on 2024-05-15 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion_producto',
            field=models.TextField(help_text='Ingrese la descripcion del producto', max_length=2000),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion_tecnica',
            field=models.TextField(help_text='Ingrese la descripcion tecnica', max_length=2000),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio_producto',
            field=models.FloatField(default=1, help_text='Ingrese el precio del producto'),
        ),
    ]
