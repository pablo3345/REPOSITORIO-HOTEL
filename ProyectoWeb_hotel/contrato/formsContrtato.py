from contrato.models import Contrato
from django import forms



class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local' 



        
        
class FormContrato(forms.ModelForm):
    
        class Meta:
            model=Contrato
            
            fields=[
                'habitacion',
                'huesped',
                'fecha_entrada',
                'fecha_salida',
                'importe_estadia',
                'importe_otros_gasto',
                'total'
                
                
                
                
                
                
            ]
            
            labels={
                'habitacion': 'Habitacion',
                'huesped': 'Huesped',
                'fecha_entrada': 'Fecha Entrada',
                'fecha_salida': 'Fecha Salida',
                'importe_estadia': "Importe estadia",
                'importe_otros_gasto': 'Importe de otros gastos',
                'total': 'Total'
                
                
            }
            
            widgets={
                
                'habitacion':forms.Select(),
                'huesped': forms.Select(),
                'fecha_entrada':DateTimeInput(), # este DateTimeInput() viene de la clase de arriba que puse para que me muestre el widgets
                'fecha_salida': DateTimeInput(),
                'importe_estadia': forms.NumberInput(attrs={'placeholder':'0,00'}),
                'importe_otros_gasto': forms.NumberInput(),
                'total': forms.NumberInput(attrs={'placeholder':'0,00'})
                
                
                
                
            }
        