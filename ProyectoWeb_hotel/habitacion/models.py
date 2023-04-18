from django.db import models

# Create your models here.

capacidad_status = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'),(11, '11'),(12, '12')] #es una tupla

class Habitacion(models.Model):

    nombre_numero =models.CharField(max_length=40)
    capacidad = models.IntegerField( null= False, blank=False, choices=capacidad_status, default= 1)#con default = 1 me aparece solo los valores que escribi arriba y no esa line discontinua que molesta)
    camita_bebe = models.CharField(max_length=4, choices=(('SI', 'SI'), ('NO', 'NO')), default=1)
    esta_limpia =  models.CharField(max_length=4, choices=(('SI', 'SI'), ('NO', 'NO')), default=1)
    posee_heladera = models.CharField(max_length=4, choices=(('SI', 'SI'), ('NO', 'NO')), default=1)
    posee_aire_acondicionado = models.CharField(max_length=4, choices=(('SI', 'SI'), ('NO', 'NO')), default=1)
    posee_calefaccion = models.CharField(max_length=4, choices=(('SI', 'SI'), ('NO', 'NO')), default=1)
    posee_ventana = models.CharField(max_length=4, choices=(('SI', 'SI'), ('NO', 'NO')), default=1)
    posee_cama_matrimonial = models.CharField(max_length=4, choices=(('SI', 'SI'), ('NO', 'NO')), default=1)
    posee_televisor = models.CharField(max_length=4, choices=(('SI', 'SI'), ('NO', 'NO')), default=1)
    posee_wifi = models.CharField(max_length=4, choices=(('SI', 'SI'), ('NO', 'NO')), default=1)
    estado_libre = models.ImageField(default="libre.jpg")  # upload_to (es para decir donde vamos a dejar las imagenes cargadas, en que directorio), null= True(para decirle que  las imagenes las podemos dejar en blanco)
    estado_ocupado = models.ImageField(default="ocupado.jpg")
    estado_post_ocupado = models.ImageField(default="despues_del_plazo.jpg")
    #-------------------------------------------------------------------------------------------------------------------
    libre = models.CharField(max_length=10, default="LIBRE")
    ocupada = models.CharField(max_length=10, default="OCUPADA")
    post_ocupada = models.CharField(max_length=10, default="POST OCUPADA")
    #-------------------------------------------------------------------------------------------------------------------
    created = models.DateTimeField(auto_now_add=True)  # aca guardamos la fecha que se creo un servicio
    updated = models.DateTimeField(auto_now=True)  # aca guardamos cuando se actualiza

    def __str__(self):
        return f'{self.nombre_numero} con capacidad de {self.capacidad}' # la f es de formato

    class Meta:
        db_table = "habitaciones"
        verbose_name = "Habitacion"
        verbose_name_plural = "Habitaciones"
        ordering = ['id']  # significa que se va a ordenar por id


