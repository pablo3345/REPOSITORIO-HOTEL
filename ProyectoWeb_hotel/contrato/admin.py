from django.contrib import admin
from .models import Huesped, Contrato

# Register your models here.


class adminHuesped(admin.ModelAdmin):
    
    readonly_fields=("created", "updated")
    
    list_display=("nombre_responsable", "apellido", "dni", "edad", "demas_huespedes", "patente_vehiculo", "correo_electronico", "created", "updated")
    
    search_fields=("nombre_responsable", "apellido")
    
    list_filter =("nombre_responsable", "apellido",)
    
    
    
    
class adminContrato(admin.ModelAdmin):
    pass



admin.site.register(Huesped, adminHuesped)
admin.site.register(Contrato, adminContrato)
    
    
