from django.contrib import admin
from .models import Proveedores

# Register your models here.

class adminProveedores(admin.ModelAdmin):
    
    readonly_fields=("created", "updated")
    
    list_display=("nombre_proveedor", "apellido", "direccion", "telefono", "mail", "nombre_empresa", "algun_otro_dato",  "created", "updated")



admin.site.register(Proveedores, adminProveedores)