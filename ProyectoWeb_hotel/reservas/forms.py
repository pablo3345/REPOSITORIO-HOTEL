from reservas.models import HuespedReserva, Reserva
from habitacion.models import Habitacion

from django import forms

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local' 





class FormHuesped_reserva(forms.ModelForm):
    
        class Meta:
            model=HuespedReserva
        
        
            fields=[
               'nombre', 
               'apellido',
               
               'dni',
              
             
               'telefono'
             
  
            
        ]
        
        
            labels={
            
               'nombre':'Nombre', 
               'apellido': 'Apellido',
              
               'dni': 'DNI',
               'telefono': 'Telefono'
             
             
            
    
            
        }
        
        
            widgets={
            
               'nombre': forms.TextInput(),
               'apellido': forms.TextInput(),
             
               'dni': forms.TextInput(),
             
              
               'telefono':forms.TextInput()
               
             
            
            
            
        }
            
class FormReserva(forms.ModelForm):
    
        # def __init__(self, *args, **kwargs):
        #         super(FormReserva, self).__init__(*args, **kwargs) # para filtrar el select de habitacion libres
        #         self.fields['habitacion'].queryset= Habitacion.objects.filter(estado="Null")
                
        
            
      
    
        class Meta:
            model=Reserva
            
            
            
            fields=[
                'habitacion',
                'huesped',
                'fecha_entrada',
                'fecha_salida',
                #'estado',
                #'importe_estadia',
                'importe_otros_gasto',
               
                'descuento_importe_noche',
                'descuento_total_calcularo',
                'aumento_total',
              
                'porcentaje_de_senia',
               # 'total_senia'
                #'late_chack_out'
               # 'total'
               
                
                
                
                
                
                
            ]
            
            labels={
                'habitacion': 'Habitacion',
                'huesped':'Huesped reserva',
                'fecha_entrada':'Fecha entrada',
                'fecha_salida': 'Fecha salida',
               # 'estado': 'Estado',
               # 'importe_estadia',
                'importe_otros_gasto':'Otros gastos',
               
                'descuento_importe_noche': 'Descuento importe de la habitación por noche',
                'descuento_total_calcularo':'Descuento al total calculado',
                'aumento_total':'Aumento al total',
              
                'porcentaje_de_senia':'Cobrar porcentaje de la reserva'
                #'total_senia'
                
                
                
            }
            
            
            widgets={
               
                'habitacion': forms.Select(),
                'huesped':forms.Select(),
                'fecha_entrada':DateTimeInput(),
                'fecha_salida':DateTimeInput(),
               # 'estado': 'Estado',
               # 'importe_estadia',
                'importe_otros_gasto': forms.NumberInput(attrs={'placeholder':'0,00'}),
               
                'descuento_importe_noche': forms.Select(),
                'descuento_total_calcularo':forms.Select(),
                'aumento_total':forms.Select(),
              
                'porcentaje_de_senia':forms.Select()
                #'total_senia'
            
        }
        