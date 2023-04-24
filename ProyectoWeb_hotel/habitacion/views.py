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
    #habitacion = Habitacion.objects.get(id=id_habitacion)

    habitacion= get_object_or_404(Habitacion, id=id_habitacion)






    if request.method == 'POST':  # si aprete el boton

        form = FormsHabitacion(request.POST)
        if form.is_valid():  # vamos a preguntar si los datos que se ingresaron son validos
            form.save()
            messages.success(request, "La habitacion se actualizo correctamente...")

            return redirect('Habitacion')


        else:
            messages.error(request, "La habitacion no se actualizo...")




    else:

        form = FormsHabitacion(instance=habitacion)
    #
    #     form = FormsHabitacion()  # si no es un post le decimos que nos vuelva a renderizar el formulario

    return render(request, 'habitacion/modificar_tabla.html', {'forms': form})












