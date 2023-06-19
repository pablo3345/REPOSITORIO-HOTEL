# Generated by Django 3.2.19 on 2023-06-19 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insumos',
            name='disponibilidad',
            field=models.BooleanField(choices=[(True, 'SI'), (False, 'NO')], default=1),
        ),
        migrations.AlterField(
            model_name='insumos',
            name='proveedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='productos.proveedores'),
        ),
        migrations.AlterField(
            model_name='producto_al_publico',
            name='disponibilidad',
            field=models.BooleanField(choices=[(True, 'SI'), (False, 'NO')], default=1),
        ),
        migrations.AlterField(
            model_name='producto_al_publico',
            name='proveedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='productos.proveedores'),
        ),
    ]
