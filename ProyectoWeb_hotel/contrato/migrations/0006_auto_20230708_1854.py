# Generated by Django 3.2.19 on 2023-07-08 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0005_auto_20230629_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='huesped',
            name='telefono',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='descuento_importe_noche',
            field=models.IntegerField(choices=[(0, '0'), (5, '5'), (10, '10'), (15, '15'), (20, '20'), (25, '25'), (30, '30'), (35, '35'), (40, '40'), (45, '45'), (50, '50'), (55, '55'), (60, '60'), (70, '70')], default=1),
        ),
    ]
