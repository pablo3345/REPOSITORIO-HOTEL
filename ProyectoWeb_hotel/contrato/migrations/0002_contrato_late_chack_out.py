# Generated by Django 3.2.19 on 2023-05-27 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='late_chack_out',
            field=models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default=1, max_length=4),
        ),
    ]