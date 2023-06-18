from django.contrib import admin
from .models import Proveedores, Insumos

# Register your models here.

class adminProveedores(admin.ModelAdmin):
    
    readonly_fields=("created", "updated")
    
    list_display=("nombre_proveedor", "apellido", "direccion", "telefono", "mail", "nombre_empresa", "algun_otro_dato",  "created", "updated")
    
    
    
class adminInsumos(admin.ModelAdmin):
    readonly_fields=("created", "updated")
    
    list_display=("nombre_insumos", "marca_insumos", "precio", "medida", "proveedor", "algun_otro_dato", "disponibilidad",  "created", "updated")
    



admin.site.register(Proveedores, adminProveedores)
admin.site.register(Insumos, adminInsumos)