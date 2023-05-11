from django.db import models
from habitacion.models import Habitacion
#from contrato.models import Huesped, Contrato

 #Create your models here.

class Huesped(models.Model):
     
    nombre_responsable =models.CharField(max_length=40)
    apellido =models.CharField(max_length=40)
    edad =models.IntegerField()
    dni= models.CharField(max_length=20)
    demas_huespedes = models.CharField(max_length= 200,  null= True, blank=True)
    patente_vehiculo= models.CharField(max_length=20,  null= True, blank=True)
    modelo_vehiculo= models.CharField(max_length=40,  null= True, blank=True)
    correo_electronico = models.EmailField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)  # aca guardamos la fecha que se creo un servicio
    updated = models.DateTimeField(auto_now=True)  # aca guardamos cuando se actualiza
    
    def __str__(self):
        return f'{self.nombre_responsable} apellido {self.apellido} dni {self.dni}' # la f es de formato

    class Meta:
        db_table = "huesped"
        verbose_name = "Huesped"
        verbose_name_plural = "Huespedes"
        ordering = ['id']  # significa que se va a ordenar por id
        
   
    
    



class Contrato(models.Model):
    
    habitacion = models.ForeignKey(Habitacion, on_delete= models.CASCADE, default=1)
    huesped = models.ForeignKey(Huesped, on_delete= models.CASCADE, default=1) #con default=1 en el select, me borra esa linea discontinua que aparece
    fecha_entrada= models.DateTimeField(auto_now=False)
    fecha_salida =models.DateTimeField(auto_now=False)
    importe_estadia = models.FloatField() # poner en un casillero el total del precio de la habitacion x noche
    importe_otros_gasto = models.FloatField(null=True, blank=True, default=0)
    total = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)  # aca guardamos la fecha que se creo un servicio
    updated = models.DateTimeField(auto_now=True)  # aca guardamos cuando se actualiza
    
    class Meta:
        db_table = "contrato"
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"
        ordering = ['id']  # significa que se va a ordenar por id
   
  


   