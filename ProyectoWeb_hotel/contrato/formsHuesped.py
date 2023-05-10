from contrato.models import Huesped
from django import forms


class FormHuesped(forms.ModelForm):
    
        class Meta:
            model=Huesped
        
        
            fields=[
               'nombre_responsable', 
               'apellido',
               'edad',
               'dni',
               'demas_huespedes',
               'patente_vehiculo',
               'modelo_vehiculo',
               'correo_electronico' 
    
  
            
        ]
        
        
            labels={
            
               'nombre_responsable':'Nombre responsable', 
               'apellido': 'Apellido',
               'edad': 'Edad',
               'dni': 'DNI',
               'demas_huespedes': 'Demas huespedes',
               'patente_vehiculo': 'Patente vehiculo',
               'modelo_vehiculo': 'Modelo vehiculo',
               'correo_electronico': 'Email'
            
            
    
            
        }
        
        
            widgets={
            
               'nombre_responsable': forms.TextInput(),
               'apellido':  forms.TextInput(),
               'edad':  forms.NumberInput(),
               'dni': forms.TextInput(),
               'demas_huespedes': forms.Textarea(),
               'patente_vehiculo': forms.TextInput(),
               'modelo_vehiculo':  forms.TextInput(),
               'correo_electronico': forms.EmailInput()
            
            
            
            
        }
        