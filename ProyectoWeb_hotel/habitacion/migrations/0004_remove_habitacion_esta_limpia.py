# Generated by Django 3.2.19 on 2023-06-23 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habitacion', '0003_alter_habitacion_capacidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habitacion',
            name='esta_limpia',
        ),
    ]
