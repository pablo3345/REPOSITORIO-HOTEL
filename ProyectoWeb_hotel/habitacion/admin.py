from django.contrib import admin
from .models import Habitacion

# Register your models here.

class HabitacionAdmin(admin.ModelAdmin):
    readonly_fields = ('estado_libre', 'estado_ocupado', 'estado_post_ocupado', 'libre', 'ocupada','post_ocupada', 'created', 'updated',)
    list_display = ("nombre_numero", "capacidad", "precio_por_noche","camita_bebe", "esta_limpia", "posee_heladera","posee_aire_acondicionado" ,"posee_calefaccion", "posee_ventana", "posee_cama_matrimonial", "posee_televisor", "posee_wifi",
                    "jacuzzi","posee_microondas", "otro_dato", "created", "updated")

    radio_fields = {'camita_bebe': admin.HORIZONTAL, 'esta_limpia': admin.HORIZONTAL, 'posee_heladera': admin.HORIZONTAL,
                    'posee_aire_acondicionado': admin.HORIZONTAL, 'posee_calefaccion': admin.HORIZONTAL, 'posee_ventana': admin.HORIZONTAL, 'posee_cama_matrimonial': admin.HORIZONTAL,
                    'posee_televisor': admin.HORIZONTAL, 'posee_wifi': admin.HORIZONTAL, 'jacuzzi': admin.HORIZONTAL, 'posee_microondas': admin.HORIZONTAL}

    search_fields = ("nombre_numero", "capacidad")
    list_filter = ("capacidad",)





admin.site.register(Habitacion, HabitacionAdmin)