# Generated by Django 3.2.19 on 2023-06-02 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitacion',
            name='estado',
            field=models.CharField(default='Null', max_length=10),
        ),
    ]
