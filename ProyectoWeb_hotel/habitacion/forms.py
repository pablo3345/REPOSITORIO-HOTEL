from habitacion.models import Habitacion
from django import forms

class FormsHabitacion(forms.ModelForm):

    class Meta:
        model = Habitacion

        fields = [  # aca en esta tupla ponemos los campos del modelo que queremos utilizar

            'nombre_numero',
            'capacidad',
            'camita_bebe',
            'esta_limpia',
            'posee_heladera',
            'posee_aire_acondicionado',
            'posee_calefaccion',
            'posee_ventana',
            'posee_cama_matrimonial',
            'posee_televisor',
            'posee_wifi',
             # 'estado_libre',
             # 'estado_ocupado',
             # 'estado_post_ocupado',

        ]

        label = {  # aca en este diccionario pongo las etiqetas que quiero que tengan los textxField en el html

            'nombre_numero': 'Nombre o numero:',
            'capacidad': 'Capacidad:',
            'camita_bebe': 'Posee camita bebe',
            'esta_limpia': 'Esta limpia:',
            'posee_heladera': 'Posee heladera en la habitacion:',
            'posee_aire_acondicionado': 'Posee aire acondicionado:',
            'posee_calefaccion': 'Posee calefaccion:',
            'posee_ventana': 'Posee ventana en la habitacion:',
            'posee_cama_matrimonial': 'Posee cama matrimonial',
            'posee_televisor': 'Posee televisor:',
            'posee_wifi': 'Posee wifi:',
            # 'estado_libre': 'Disponible:',
            # 'estado_ocupado': 'Ocupada:',
            # 'estado_post_ocupado':'Plazo vencido:',

        }

        widgets = {  # lo que se va a ver en el formulario del html
            'nombre_numero': forms.TextInput(),
            'capacidad': forms.Select(),

            'camita_bebe': forms.RadioSelect(),

            'esta_limpia': forms.RadioSelect(),
            'posee_heladera': forms.RadioSelect(),
            'posee_aire_acondicionado': forms.RadioSelect(),
            'posee_calefaccion':forms.RadioSelect(),
            'posee_ventana':forms.RadioSelect(),
            'posee_cama_matrimonial': forms.RadioSelect(),
            'posee_televisor': forms.RadioSelect(),
            'posee_wifi': forms.RadioSelect(),
            # 'estado_libre':  forms.FileInput(),
            # 'estado_ocupado': forms.FileInput(),
            # 'estado_post_ocupado': forms.FileInput(),

        # attrs={'class':'form-row'} poner en () ejemplo TextInput() seria la clase de bootdtrap
        # attrs={'placeholder':'Phone Number'} poner esto en el text input en gris pero que se puede escribir arriba de la palabra
        }