from django.shortcuts import render, redirect, get_object_or_404
from habitacion.forms import FormsHabitacion
from django.contrib import messages
from .models import Habitacion

# Create your views here.
def mostrarHabitacion(request):



          if request.method == 'POST': #si aprete el boton


               form = FormsHabitacion(request.POST)
               if form.is_valid():  # vamos a preguntar si los datos que se ingresaron son validos
                   form.save()
                   messages.success(request, "La habitacion se guardo correctamente...")

                   return redirect('Habitacion')


               else:
                   messages.error(request, "La habitacion no se ha guardado...")



          else:

                form = FormsHabitacion()  # si no es un post le decimos que nos vuelva a renderizar el formulario


          return render(request, 'habitacion/habitacion.html', {'forms': form})




def actualizarHabitacion(request):
    habitaciones = Habitacion.objects.all()



    return render(request, 'habitacion/modificarHabitacion.html', {'habitaciones': habitaciones})





def tabla_modificar(request, id_habitacion):

    habitacion = get_object_or_404(Habitacion, id=id_habitacion)

    if request.method == "POST":
                       #------CAMPOS DEL FORMULARIO.---------------

        nombre = request.POST.get("nombre_numero")
        capacidad = request.POST.get("capacidad")
        camita_bebe = request.POST.get("camita_bebe")
        esta_limpia = request.POST.get("esta_limpia")
        posee_heladera = request.POST.get("posee_heladera")
        posee_aire_acondicionado = request.POST.get("posee_aire_acondicionado")
        posee_calefaccion = request.POST.get("posee_calefaccion")
        posee_ventana = request.POST.get("posee_ventana")
        posee_cama_matrimonial = request.POST.get("posee_cama_matrimonial")
        posee_televisor = request.POST.get("posee_televisor")
        posee_wifi = request.POST.get("posee_wifi")

        #-----------------CAMPOS DEL MODELO--------------------------------------------

        habitacion.nombre_numero = nombre
        habitacion.capacidad = capacidad
        habitacion.camita_bebe = camita_bebe
        habitacion.esta_limpia = esta_limpia
        habitacion.posee_heladera = posee_heladera
        habitacion.posee_aire_acondicionado = posee_aire_acondicionado
        habitacion.posee_calefaccion = posee_calefaccion
        habitacion.posee_ventana = posee_ventana
        habitacion.posee_cama_matrimonial = posee_cama_matrimonial
        habitacion.posee_televisor = posee_televisor
        habitacion.posee_wifi = posee_wifi

        try:
            habitacion.save()
            messages.success(request, "La habitacion se actualizo correctamente...")

        except:

            messages.error(request, "La habitacion no se actualizo...")




        return redirect('modificarHabitacion')

    else:
        form = FormsHabitacion(instance=habitacion)

    return render(request, 'habitacion/modificar_tabla.html', {'form': form})






































