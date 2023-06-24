from django.shortcuts import render, redirect, get_object_or_404
from habitacion.forms import FormsHabitacion
from django.contrib import messages
from .models import Habitacion
from contrato.models import Contrato

# Create your views here.
def mostrarHabitacion(request):
    habitacion = Habitacion()
    
   



    if request.method == 'POST': #si aprete el boton
       
       

        form = FormsHabitacion(request.POST)
              
        if form.is_valid():  # vamos a preguntar si los datos que se ingresaron son validos
            
            #---------------le agrrego esto para probar..----------
           
           
                           
               
            form.save()
            
           # No_Limpia(request)   
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
        precio_por_noche = request.POST.get("precio_por_noche")
        camita_bebe = request.POST.get("camita_bebe")
        #esta_limpia = request.POST.get("esta_limpia")
        posee_heladera = request.POST.get("posee_heladera")
        posee_aire_acondicionado = request.POST.get("posee_aire_acondicionado")
        posee_calefaccion = request.POST.get("posee_calefaccion")
        posee_ventana = request.POST.get("posee_ventana")
        posee_cama_matrimonial = request.POST.get("posee_cama_matrimonial")
        posee_televisor = request.POST.get("posee_televisor")
        posee_wifi = request.POST.get("posee_wifi")
        posee_jacuzzi = request.POST.get("jacuzzi")#lo agregue nuevo
        posee_microondas =request.POST.get("posee_microondas")#lo agregue nuevo
        check_out_late =request.POST.get("check_out_lates")#lo agregue nuevo
        otro_dato = request.POST.get("otro_dato")#lo agregue nuevo

        #-----------------CAMPOS DEL MODELO--------------------------------------------

        habitacion.nombre_numero = nombre
        habitacion.capacidad = capacidad
        habitacion.precio_por_noche = precio_por_noche
        habitacion.camita_bebe = camita_bebe
       # habitacion.esta_limpia = esta_limpia
        habitacion.posee_heladera = posee_heladera
        habitacion.posee_aire_acondicionado = posee_aire_acondicionado
        habitacion.posee_calefaccion = posee_calefaccion
        habitacion.posee_ventana = posee_ventana
        habitacion.posee_cama_matrimonial = posee_cama_matrimonial
        habitacion.posee_televisor = posee_televisor
        habitacion.posee_wifi = posee_wifi
        habitacion.jacuzzi=posee_jacuzzi
        habitacion.posee_microondas=posee_microondas
        habitacion.check_out_lates=check_out_late
        habitacion.otro_dato=otro_dato
        
        #....................................le agregue esto antes no estaba-----------------
       
       

        try:
            habitacion.save()
          
            messages.success(request, "La habitacion se actualizo correctamente...")

        except:

            messages.error(request, "La habitacion no se actualizo...")




        return redirect('modificarHabitacion')

    else:
        form = FormsHabitacion(instance=habitacion)

    return render(request, 'habitacion/modificar_tabla.html', {'form': form})


def eliminarHabitacion(request, id_habitacion):
    
    
    habitacion = get_object_or_404(Habitacion, id=id_habitacion)
    #eliminar_y_Poner_Null(request, id_habitacion)
    
    try:
        habitacion.delete()
       
        messages.success(request, "La habitacion se elimino correctamente...")
        
    except:
        messages.error(request, "La habitacion no se elimino...")
        
    return redirect('modificarHabitacion')




def No_Limpia(request):
   # habitacion = Habitacion()
    #form = FormsHabitacion()
    habitaciones = Habitacion.objects.all()
    esta_limpia = request.POST.get("esta_limpia")
    
    if request.method == 'POST':
        for habi in habitaciones:
            if habi.esta_limpia=="NO":
                habi.estado="ocupada"
                habi.save()
        
        
       
def habilitar_NoLimpias(request, id_habitacion):
    habitacion = get_object_or_404(Habitacion, id=id_habitacion)
    
    if habitacion.esta_limpia=="NO" and habitacion.estado=="ocupada":
        habitacion.estado="Null"
        habitacion.esta_limpia="SI"
        habitacion.save()
        
        return redirect('Panel')
    
    
    
def habilitarPost_time(reuest, id_habitacion):
    habitacion = get_object_or_404(Habitacion, id=id_habitacion)
    contrato = Contrato.objects.all()
     
    False_variable = False
    
    if habitacion.estado=="ocupada":
        habitacion.estado="Null"
        habitacion.save()
        
        #-------------le greguego esto------------------------
            
        for contr in contrato:
                 
            if contr.habitacion== habitacion:
                contr.estado= False_variable
                contr.save()
        return redirect('Panel')
    
    
    


    
   
      
       
        
    
    
        
    
   
    
    






































