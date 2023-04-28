from django.db import models

 #Create your models here.

class Huesped(models.Model):
     
    nombre_responsable =models.CharField(max_length=40)
    apellido =models.CharField(max_length=40)
    edad =models.IntegerField()
    dni= models.CharField(max_length=20)
    demas_huespedes = models.CharField(max_length= 200,  null= True, blank=True)
    patente_vehiculo= models.CharField(max_length=20,  null= True, blank=True)
    correo_electronico = models.EmailField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)  # aca guardamos la fecha que se creo un servicio
    updated = models.DateTimeField(auto_now=True)  # aca guardamos cuando se actualiza
    
    def __str__(self):
        return f'{self.nombre_responsable} apellido {self.apellido}' # la f es de formato

    class Meta:
        db_table = "huesped"
        verbose_name = "Huesped"
        verbose_name_plural = "Huespedes"
        ordering = ['id']  # significa que se va a ordenar por id
    
    
    



class Contrato(models.Model):


    pass