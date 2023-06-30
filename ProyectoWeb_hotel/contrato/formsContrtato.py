from contrato.models import Contrato
from django import forms
from habitacion.models import Habitacion



class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local' 



        
        
class FormContrato(forms.ModelForm):
    
        def __init__(self, *args, **kwargs):
                super(FormContrato, self).__init__(*args, **kwargs) # para filtrar el select de habitacion libres
                self.fields['habitacion'].queryset= Habitacion.objects.filter(estado="Null")
                
        
            
      
    
        class Meta:
            model=Contrato
            
            
            
            fields=[
                'habitacion',
                'huesped',
                'fecha_entrada',
                'fecha_salida',
                #'importe_estadia',
                'importe_otros_gasto',
                'descuento_importe_noche',
                'descuento_total_calcularo',
                'aumento_total',
                #'late_chack_out'
               # 'total'
               
                
                
                
                
                
                
            ]
            
            labels={
                'habitacion': 'Habitacion (libres)',
                'huesped': 'Huesped',
                'fecha_entrada': 'Fecha Entrada',
                'fecha_salida': 'Fecha Salida',
                'importe_estadia': "Importe estadia se agrega automaticamente",
                'importe_otros_gasto': 'Gastos extras (dejar en cero si no hay importe)',
                'descuento_importe_noche':'Hacer descuento  al precio de la habitacion por noche',
                'descuento_total_calcularo':'Hacer descuento al total calculado',
                'aumento_total': 'Hacer un aumento al total',
                #'late_chack_out':'Late check out',
                'total': 'Total se agrega automaticamente'
                
                
                
            }
            
            widgets={
                
                'habitacion':forms.Select(),
                'huesped': forms.Select(),
                'fecha_entrada':DateTimeInput(), # este DateTimeInput() viene de la clase de arriba que puse para que me muestre el widgets
                'fecha_salida': DateTimeInput(),
                'importe_estadia': forms.NumberInput(attrs={'readonly':True,'hidden': True,'required': False}),
                'importe_otros_gasto': forms.NumberInput(attrs={'placeholder':'0,00'}),
                'descuento_importe_noche': forms.Select(),
                'descuento_total_calcularo': forms.Select(),
                'aumento_total': forms.Select(),
                
               # 'late_chack_out':  forms.RadioSelect(),
                'total': forms.NumberInput(attrs={'readonly':True,'hidden': True,'required': False})
               
                
                
                
                
            }
