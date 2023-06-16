# Generated by Django 3.2.19 on 2023-06-15 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proveedor', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=40)),
                ('telefono', models.CharField(max_length=40)),
                ('mail', models.EmailField(blank=True, max_length=254, null=True)),
                ('nombre_empresa', models.CharField(max_length=40)),
                ('algun_otro_dato', models.CharField(blank=True, max_length=40, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'db_table': 'proveedores',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Producto_al_publico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=40)),
                ('marca_producto', models.CharField(max_length=40)),
                ('precio_al_publico', models.FloatField()),
                ('precio_de_costo', models.FloatField()),
                ('medida', models.FloatField()),
                ('disponibilidad', models.BooleanField(choices=[('SI', True), ('NO', False)], default=1)),
                ('precio_promocion', models.FloatField(default=0.0)),
                ('algun_otro_dato', models.CharField(blank=True, max_length=40, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.proveedores')),
            ],
            options={
                'verbose_name': 'Producto al publico',
                'verbose_name_plural': 'Productos al publico',
                'db_table': 'producto_al_publico',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Insumos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_insumos', models.CharField(max_length=40)),
                ('marca_insumos', models.CharField(max_length=40)),
                ('precio', models.FloatField()),
                ('medida', models.FloatField()),
                ('algun_otro_dato', models.CharField(blank=True, max_length=40, null=True)),
                ('disponibilidad', models.BooleanField(choices=[('SI', True), ('NO', False)], default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.proveedores')),
            ],
            options={
                'verbose_name': 'Insumo',
                'verbose_name_plural': 'Insumos',
                'db_table': 'insumos',
                'ordering': ['id'],
            },
        ),
    ]