from django.db import models
from habitacion.models import Habitacion
import datetime
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
        return f'{self.nombre_responsable}  {self.apellido} dni {self.dni}' # la f es de formato

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
    importe_otros_gasto = models.FloatField()
    total = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)  # aca guardamos la fecha que se creo un servicio
    updated = models.DateTimeField(auto_now=True)  # aca guardamos cuando se actualiza
    
    class Meta:
        db_table = "contrato"
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"
        ordering = ['id']  # significa que se va a ordenar por id
        
        
        
    def calcularFechas(request, fecha_entra, fecha_sali):
       
        
        fechaConvertida = datetime.datetime.strptime(fecha_entra, '%Y-%m-%dT%H:%M') # strptime lo convierto a objeto datetime, el segundo parametro le dice como interpretar la fecha, cual es la hora, el dia, el mes etc
        fechaConvertida2 = datetime.datetime.strptime(fecha_sali, '%Y-%m-%dT%H:%M')
         
        diferencia = fechaConvertida2-fechaConvertida 
        
        
          #--------------------------check out 10--------------------------
        if fechaConvertida2.hour ==10 and fechaConvertida2.minute ==00:
       
          if fechaConvertida.hour <10 and diferencia.days >00:
            
            diferenciaConvertida = diferencia.days
            diferenciaConvertida = diferenciaConvertida #+1
            print(diferenciaConvertida)
       
         
          elif fechaConvertida.hour >= 10 and fechaConvertida.minute>=1: #le agregue el = al 00
            
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida+1 #+2
              print(diferenciaConvertida, "(10) debo sumarle uno")
             
          elif fechaConvertida.hour ==10 and fechaConvertida.minute ==00:
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida #+1
         
              print("igual a 10 (10)", diferenciaConvertida)
              
          
             
        
          elif diferencia.days <1:
               diferenciaConvertida=1
               print("menos de un dia (10)", diferenciaConvertida)
               
          elif fechaConvertida.hour >= 10: #le agregue el = al 00
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida+1 #+2
              print(diferenciaConvertida, "(10) debo sumarle uno, para la hora 22")
              
              
      
             #---------------------late check out--------------------
             
        diferenciaGlobal = diferenciaConvertida
        diferenciaGlobal_late = diferenciaGlobal+0.5
        print(diferenciaGlobal, "diferencia global")
        print(diferenciaGlobal_late, "diferencia global late")
        
        return diferenciaGlobal
        
        
       
         
           
             
    

    
             
       
             
    
             
             
            
             
             
       
             
    
             
             
            
             
             
       
        
    
   
  


   