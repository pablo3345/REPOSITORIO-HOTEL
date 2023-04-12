from habitacion.models import Habitacion
from django import forms

class FormsHabitacion(forms.ModelForm):

    class Meta:
        model = Habitacion

        fields = [  # aca en esta tupla ponemos los campos del modelo que queremos utilizar

            'nombre_numero',
            'capacidad',
            'cochecito_bebe',
            'si_esta_limpia',
            'si_posee_heladera',
            'si_posee_aire_acondicionado',
            'si_posee_calefaccion',
            'si_posee_ventana',
            'estado_libre',
            'estado_ocupado',
            'estado_post_ocupado',

        ]

        label = {  # aca en este diccionario pongo las etiqetas que quiero que tengan los textxField en el html

            'nombre_numero': 'Nombre o numero:',
            'capacidad': 'Capacidad:',
            'si_esta_limpia': 'Si esta limpia:',
            'si_posee_heladera': 'Posee heladera en la habitacion:',
            'si_posee_aire_acondicionado': 'Posee aire acondicionado en la habitacion:',
            'si_posee_calefaccion': 'Posee calefaccion en la habitacion:',

            'si_posee_ventana': 'Posee ventana en la habitacion:',
            'estado_libre': 'Disponible:',
            'estado_ocupado': 'Ocupada:',
            'estado_post_ocupado':'Plazo vencido:',

        }

        widgets = {  # lo que se va a ver en el formulario del html
            'nombre_numero': forms.TextInput(),
            'capacidad': forms.Select(),
            'cochecito_bebe': forms.RadioSelect(),

            'si_esta_limpia': forms.RadioSelect(),
            'si_posee_heladera': forms.RadioSelect(),
            'si_posee_aire_acondicionado': forms.RadioSelect(),
            'si_posee_calefaccion':forms.RadioSelect(),
            'si_posee_ventana':forms.RadioSelect(),
            'estado_libre':  forms.ClearableFileInput(),
            'estado_ocupado': forms.ClearableFileInput(),
            'estado_post_ocupado': forms.ClearableFileInput(),

        # attrs={'class':'form-row'} poner en () ejemplo TextInput() seria la clase de bootdtrap
        # attrs={'placeholder':'Phone Number'} poner esto en el text input en gris pero que se puede escribir arriba de la palabra
        }