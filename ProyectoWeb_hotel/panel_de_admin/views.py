from django.shortcuts import render
from habitacion.models import Habitacion
from contrato.models import Contrato
import datetime

# Create your views here.

def mostrarPanel(request):
  
  
    habitacion = Habitacion.objects.all()
    contrato = Contrato.objects.all()
    #habitacion = Habitacion()
    
    
    #  #---------------------------------------timeDelta-----------------------------------------------
    #fecha_sali = request.POST.get("fecha_salida")

     
    #fechaConvertida2 = datetime.datetime.strptime(fecha_sali, '%Y-%m-%dT%H:%M')
   
    #dia_delta = datetime.timedelta(seconds=1)
    #fechaFutura = fechaConvertida2+dia_delta
    
     #-----------------------------------------------------------------------------------------------
  
    
    
    habitacionesLibres = list()
   # habitacionesPostOcupadas = list()
    habitacionesNoLimpias = list()
    #----------------------------
    habitaciones_post = list()
    habitacionesOcupadas = list()
    
    
    for habi in habitacion:
      if habi.estado =="Null" and habi.esta_limpia =="SI":
          habitacionesLibres.append(habi)
          
      
          
          
    for habi2 in habitacion:
      if habi2.esta_limpia =="NO" and habi2.estado=="Null":
          habitacionesNoLimpias.append(habi2)
         
          
    
          
        
    for contra in contrato:
       fecha_sali = contra.fecha_salida
       hoy = datetime.datetime.now()
       #fechaConvertida2 = datetime.datetime.strptime(fecha_sali, '%Y-%m-%dT%H:%M')
      # dia_delta = datetime.timedelta(seconds=1)
      # fecha_futura = fecha_sali+dia_delta
       print("fecha sali panel de control", fecha_sali, "y now", hoy)
      
      
      
       if hoy >= fecha_sali:
         
          habitaciones_post.append(contra)
          
       
       elif  fecha_sali > hoy:
           habitacionesOcupadas.append(contra)
         
           
        
         
   
    
    return render(request, "panel_de_admin/index.html", {'habitacion': habitacionesLibres, 'contrato': contrato, 'habitacionesNoLimpias': habitacionesNoLimpias,
 'habitaciones_post':habitaciones_post, 'habitacionesOcupadas': habitacionesOcupadas})




def mostrarDiagramas(request):
    
    
     return render(request, "panel_de_admin/diagramas.html")
    
    
    
    
    