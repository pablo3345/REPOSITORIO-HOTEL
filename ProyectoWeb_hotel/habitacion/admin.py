from django.contrib import admin
from .models import Habitacion

# Register your models here.

class HabitacionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ("nombre_numero", "capacidad", "cochecito_bebe", "si_esta_limpia", "si_posee_heladera","si_posee_aire_acondicionado" ,"si_posee_calefaccion", "si_posee_ventana","estado_libre","estado_ocupado",
                    "estado_post_ocupado", "created", "updated")
    radio_fields = {'cochecito_bebe': admin.HORIZONTAL, 'si_esta_limpia': admin.HORIZONTAL, 'si_posee_heladera': admin.HORIZONTAL,
                    'si_posee_aire_acondicionado': admin.HORIZONTAL, 'si_posee_calefaccion': admin.HORIZONTAL, 'si_posee_ventana': admin.HORIZONTAL}







admin.site.register(Habitacion, HabitacionAdmin)