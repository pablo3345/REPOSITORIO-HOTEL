from django.shortcuts import render
from habitacion.forms import FormsHabitacion

# Create your views here.
def mostrarHabitacion(request):

     forms = FormsHabitacion

     return render(request, "habitacion/habitacion.html", {'forms': forms})