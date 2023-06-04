from django.shortcuts import render
from habitacion.models import Habitacion
from contrato.models import Contrato

# Create your views here.

def mostrarPanel(request):
    habitacion = Habitacion.objects.all()
    contrato = Contrato.objects.all()
    #habitacion = Habitacion()
    
    habitacionesLibres = list()
    habitacionesOcupadas = list()
    
    
    for habi in habitacion:
      if habi.estado =="Null":
          habitacionesLibres.append(habi)
          
          
    """ for habi in habitacion:
      if habi.estado =="ocupada":
          habitacionesOcupadas.append(habi)
           """
          
    
          
        
    
    
    
   
   
    
    
  
    
   
    
    return render(request, "panel_de_admin/index.html", {'habitacion': habitacionesLibres, 'contrato': contrato})




def mostrarDiagramas(request):
    
    
     return render(request, "panel_de_admin/diagramas.html")
    
    
    
    
    