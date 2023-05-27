from django.shortcuts import render
from habitacion.models import Habitacion

# Create your views here.

def mostrarPanel(request):
    habitacion = Habitacion.objects.all()
    
    return render(request, "panel_de_admin/index.html", {'habitacion': habitacion})
    
    
    