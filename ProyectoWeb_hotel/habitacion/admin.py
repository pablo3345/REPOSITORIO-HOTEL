from django.contrib import admin
from .models import Habitacion

# Register your models here.

class HabitacionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ("nombre_numero", "capacidad", "camita_bebe", "esta_limpia", "posee_heladera","posee_aire_acondicionado" ,"posee_calefaccion", "posee_ventana", "posee_cama_matrimonial", "posee_televisor", "posee_wifi")

    radio_fields = {'camita_bebe': admin.HORIZONTAL, 'esta_limpia': admin.HORIZONTAL, 'posee_heladera': admin.HORIZONTAL,
                    'posee_aire_acondicionado': admin.HORIZONTAL, 'posee_calefaccion': admin.HORIZONTAL, 'posee_ventana': admin.HORIZONTAL, 'posee_cama_matrimonial': admin.HORIZONTAL,
                    'posee_televisor': admin.HORIZONTAL, 'posee_wifi': admin.HORIZONTAL}

    search_fields = ("nombre_numero", "capacidad")
    list_filter = ("capacidad",)





admin.site.register(Habitacion, HabitacionAdmin)