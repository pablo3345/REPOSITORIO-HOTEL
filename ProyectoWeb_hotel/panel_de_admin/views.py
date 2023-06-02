from django.shortcuts import render
from habitacion.models import Habitacion
from contrato.models import Contrato

# Create your views here.

def mostrarPanel(request):
    habitacion = Habitacion.objects.all()
    contrato = Contrato.objects.all()
    
    return render(request, "panel_de_admin/index.html", {'contrato': contrato, 'habitacion': habitacion})




def mostrarDiagramas(request):
    
    
     return render(request, "panel_de_admin/diagramas.html")
    
    
    
    
    