from django.contrib import admin
from .models import Huesped, Contrato

# Register your models here.


class adminHuesped(admin.ModelAdmin):
    
    readonly_fields=("created", "updated")
    
    list_display=("nombre_responsable", "apellido", "dni", "edad", "demas_huespedes", "patente_vehiculo", "modelo_vehiculo", "correo_electronico", "created", "updated")
    
    search_fields=("nombre_responsable", "apellido")
    
    list_filter =("nombre_responsable", "apellido",)
    
    
    
    
class adminContrato(admin.ModelAdmin):
    readonly_fields=("created", "updated")
    list_display=("habitacion", "huesped", "fecha_entrada", "fecha_salida", "importe_estadia", "importe_otros_gasto","estado", "total")
    search_fields=("habitacion", "huesped")
    list_filter=("habitacion", "huesped")



admin.site.register(Huesped, adminHuesped)
admin.site.register(Contrato, adminContrato) 
    
    
