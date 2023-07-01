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
    #-----------traer el ultimo elemento de la lista----------
    ultimo_ocupado=list()
    ultimo_Post=list()
   
    
    
    
    for habi in habitacion:
      if habi.estado =="Null": # and habi.esta_limpia =="SI": (le saques esto al if)
          habitacionesLibres.append(habi)
          
      
          
          
    """  for habi2 in habitacion:
      if habi2.esta_limpia =="NO" and habi2.estado=="ocupada":
          habitacionesNoLimpias.append(habi2)
          """
          
    
          
        
    for contra in contrato:
       fecha_sali = contra.fecha_salida
       hoy = datetime.datetime.now()
       #fechaConvertida2 = datetime.datetime.strptime(fecha_sali, '%Y-%m-%dT%H:%M')
      # dia_delta = datetime.timedelta(seconds=1)
      # fecha_futura = fecha_sali+dia_delta
     
      
      
      
       if hoy >= fecha_sali and contra.habitacion.estado == "ocupada" and contra.estado==True: # le agregue el true
         
          habitaciones_post.append(contra)
         # ultimo_Post= habitaciones_post[-1]
        
       
       elif  fecha_sali > hoy and contra.habitacion.estado == "ocupada" and contra.estado==True:
           habitacionesOcupadas.append(contra)
          # ultimo_ocupado= habitacionesOcupadas[-1]
          
        
         
   
    
    return render(request, "panel_de_admin/index.html", {'habitacion': habitacionesLibres, 'contrato': contrato, 'habitacionesNoLimpias': habitacionesNoLimpias,
 'habitaciones_post':habitaciones_post, 'habitacionesOcupadas': habitacionesOcupadas})




def mostrarDiagramas(request):
    
    
     return render(request, "panel_de_admin/diagramas.html")
    
    
    
    
    