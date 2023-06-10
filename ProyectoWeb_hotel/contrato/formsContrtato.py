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
                #'late_chack_out'
               # 'total'
               
                
                
                
                
                
                
            ]
            
            labels={
                'habitacion': 'Habitacion',
                'huesped': 'Huesped',
                'fecha_entrada': 'Fecha Entrada',
                'fecha_salida': 'Fecha Salida',
                'importe_estadia': "Importe estadia se agrega automaticamente",
                'importe_otros_gasto': 'Gastos extras (poner cero si no hay importe)',
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
               # 'late_chack_out':  forms.RadioSelect(),
                'total': forms.NumberInput(attrs={'readonly':True,'hidden': True,'required': False})
               
                
                
                
                
            }
