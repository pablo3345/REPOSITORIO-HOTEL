from productos.models import Proveedores, Insumos, Producto_al_publico
from django import forms

class ProveedoresForm(forms.ModelForm):
    
    class Meta:
        model= Proveedores
        
        fields= [
                'nombre_proveedor',
                'apellido',
                'direccion',
                'telefono',
                'mail',
                'nombre_empresa',
                'algun_otro_dato',
            
            
                           ]
        
        labels={
                'nombre_proveedor': 'Nombre',
                'apellido': 'Apellido',
                'direccion': 'Direccion',
                'telefono': 'Telefono',
                'mail': 'email',
                'nombre_empresa': 'Nombre empresa',
                'algun_otro_dato': 'Algun otro dato'
            
            
            
        }
        
        widgets={
            
            
            'nombre_proveedor':  forms.TextInput(),
            'apellido': forms.TextInput(),
            'direccion':  forms.TextInput(),
            'telefono': forms.TextInput(),
            'mail': forms.EmailInput(),
            'nombre_empresa': forms.TextInput(),
            'algun_otro_dato':  forms.TextInput(),
        }
            
            
            
        

