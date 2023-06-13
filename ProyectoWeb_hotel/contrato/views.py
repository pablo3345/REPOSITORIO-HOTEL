from django.shortcuts import render, redirect, get_object_or_404
from contrato.formsContrtato import FormContrato 
from contrato.formsHuesped import FormHuesped
from django.contrib import messages
from contrato.models import Huesped, Contrato
import datetime
from habitacion.models import Habitacion
from panel_de_admin.views import mostrarPanel


# Create your views here.


def mostrarContrato(request):
     form = FormHuesped()
     form2 = FormContrato()
     
     
     if request.method =='POST':
         
          formHuesped =FormHuesped(request.POST)
         
          if formHuesped.is_valid():
              
              formHuesped.save()
              messages.success(request, "El huesped se guardo correctamente...")
              
          else:
              messages.error(request, "El huesped no se guardo...")
              
          return redirect('Contrato')
     
     else:
          formHuesped=FormHuesped()
  
    
     return render(request, "contrato/contrato.html", {'formHuesped': form, 'formContrato': form2})
 
 
 
def modificarHuesped(request):
     #formHuesped = FormHuesped()
     huespedes = Huesped.objects.all()
     
     return render(request, "contrato/modificarHuesped.html",{'huespedes': huespedes})
     
  



def modificarTablaHuesped(request, id_huesped):
     
     formHuesped = FormHuesped()
     huesped =  get_object_or_404(Huesped, id=id_huesped)
     
     nombre_resp = request.POST.get("nombre_responsable")
     apelli = request.POST.get("apellido")
     edadd = request.POST.get("edad")
     dnii = request.POST.get("dni")
     demas_huespe = request.POST.get("demas_huespedes")
     patente_vehicu = request.POST.get("patente_vehiculo")
     modelo_vehicu = request.POST.get("modelo_vehiculo")
     correo_electro =request.POST.get("correo_electronico")
     
     if request.method =='POST':
          
          huesped.nombre_responsable= nombre_resp
          huesped.apellido = apelli
          huesped.edad = edadd
          huesped.dni = dnii
          huesped.demas_huespedes = demas_huespe
          huesped.patente_vehiculo= patente_vehicu
          huesped.modelo_vehiculo= modelo_vehicu
          huesped.correo_electronico= correo_electro
          
         
          
          try:
          
            huesped.save()
            messages.success(request, "El huesped se actualizo correctamente...")
          
            
       
        
          except:
               messages.error(request, "El huesped no se actualizo...")
               
          return redirect('modificarHuesped')
     
     
     else:
          formHues = FormHuesped(instance=huesped)
          
          
     return render(request, "contrato/modificar_tablaHuesped.html", {'formHues': formHues})



def eliminarHuesped(request, id_huesped):
     
     huesped = get_object_or_404(Huesped, id=id_huesped)
     
     try:
          huesped.delete()
          messages.success(request, "El huesped se elimino correctamente...")
          
     except:
          messages.error(request, "El huesped no se elimino...")
          
          
     return redirect('modificarHuesped')


          
     
     #---------------------------------VISTA CONTRATO--------------------------------------
     
     

         
   
     #----------------------------------------------------------------------------------------------------
def guardarContrato(request):
     form = FormHuesped()
     form2 = FormContrato()
     contrato = Contrato()
     
     true_variable = True
     
    # habitacion = Habitacion.objects.get(id= id_habitacion)
    
    
    
     
     # si en el formulario no obtengo los datos con form(request.POST), no voy a preguntar si el forn is_valid()
     
     
     if request.method == "POST":
         # habitacion=models.Habitacion.objects.get(habitacion)
          habitacions = request.POST.get("habitacion")
          huespeds =request.POST.get("huesped")
          fecha_entra = request.POST.get("fecha_entrada")
          fecha_sali = request.POST.get("fecha_salida")
          importe_estad= request.POST.get("importe_estadia")
          importe_otros_gast= request.POST.get("importe_otros_gasto")
          totals= request.POST.get("total")
          late_check_out = request.POST.get("late_chack_out")
     #.........................cambiar formato calendario.....................
          fechaConvertida = datetime.datetime.strptime(fecha_entra, '%Y-%m-%dT%H:%M') # strptime lo convierto a objeto datetime, el segundo parametro le dice como interpretar la fecha, cual es la hora, el dia, el mes etc
     
          fechaFormateada = fechaConvertida.strftime('%Y-%m-%dT%H:%M') # strftime para darle el formato que quiero
       
        
          fechaConvertida2 = datetime.datetime.strptime(fecha_sali, '%Y-%m-%dT%H:%M')
          fechaFormateada2 = fechaConvertida2.strftime('%Y-%m-%dT%H:%M') 
          
          habitacion = Habitacion.objects.get(id= habitacions)
          huesped = Huesped.objects.get(id=huespeds)
          
          #-------------------------id contrato para ponerle True----------------------
          id_contrato = contrato.id
          
          #-------fuera del horario----------
          if fechaConvertida2.hour <10 or fechaConvertida2.hour>=17:
                messages.error(request, "El horario no corresponde")
                return redirect('Contrato')
          
        
          
          
          total =calcularTotal(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
          importeEstadia =calcularImporteEstadia(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
          diferenciaConvertida = contrato.nochesDeEstadia(fecha_entra, fecha_sali, habitacions, importe_otros_gast)
        
           
        
             
        
       
          
          contrato.habitacion =habitacion # obtuve la habitacion mediante el id
          
          contrato.huesped = huesped
          contrato.fecha_entrada= fechaFormateada
          contrato.fecha_salida = fechaFormateada2
          contrato.importe_estadia= importeEstadia
          contrato.importe_otros_gasto = importe_otros_gast
          #----------------poner true cuando guardo el estado--------------
          contrato.estado=true_variable
        # contrato.late_chack_out = late_check_out #lo agregue nuevo
          contrato.total = total
          #-----------le agregue esto para probar--------------
         
        
          
          """  if total==0:
               return redirect("Inicio")
           """
          
          
               
          
          
         
          try:
          
           
        
           ponerTrue_alUltimoContrato(request, habitacions)
           ponerOcupada_ultimaHabitacion(request, habitacions)
          
           
           
           
           print("el total es total", total)
           contrato.save()
           #habitacionOcupada(request, habitacions)
           
          
        
           messages.success(request, "El contrato se guardo correctamente...")
          
               
            
           
           
          except:
               messages.error(request, "El contrato no se guardo...")
               
               
        
             
                    
      
             
          
     else:
         form2 = FormContrato()
     
     
     
     return render(request, "contrato/contrato.html", {'formHuesped': form, 'formContrato': form2, 'total': total, 'importe_de_otros_gastos':importe_otros_gast, 'importe_estadia':importeEstadia, 'diferenciaConvertida':diferenciaConvertida})
     
     
   
               
              
             
def modificarContrato(request):
          
     contratos = Contrato.objects.all()
     true = True
     contratos_true = list()
     
     for contrato in contratos:
          if contrato.estado== true:
               contratos_true.append(contrato)
     
     return render(request, "contrato/modificarContrato.html",{'contratos': contratos_true})  



def modificarTablaContrato(request, id_contrato):
       #contrato = Contrato()
     formContrato = FormContrato()
     
     contrato = get_object_or_404(Contrato, id=id_contrato)
     
     habitacion_para_form = contrato.habitacion
     
    
     
    
     
     
     #.....................................ahora obtengo el huesped y el contrato mediante el id........................
   
     
     if request.method == "POST":
          #contrato = get_object_or_404(Contrato, id=id_contrato)
          variable_true = True
     
          habitacions = contrato.habitacion.id
          huespeds =request.POST.get("huesped")# id
     
         # fecha_entra = request.POST.get("fecha_entrada")
          fecha_sali = request.POST.get("fecha_salida")
          fecha_entra = request.POST.get("fecha_entrada")
         # importe_estad= request.POST.get("importe_estadia")
          importe_otros_gast= request.POST.get("importe_otros_gasto")
         # late_check_out = request.POST.get("late_chack_out")
          #totals= request.POST.get("total")
         # habitacion = Habitacion.objects.get(id= habitacions)
         # huesped = Huesped.objects.get(id=huespeds)
          id_habitacion = contrato.habitacion.id
          habitacion = get_object_or_404(Habitacion, id=id_habitacion)
          
        
          fechaConvertida = datetime.datetime.strptime(fecha_entra, '%Y-%m-%dT%H:%M')
     
          fechaConvertida2 = datetime.datetime.strptime(fecha_sali, '%Y-%m-%dT%H:%M')
          fechaFormateada2 = fechaConvertida2.strftime('%Y-%m-%dT%H:%M') 
          
          fechaFormateada = fechaConvertida.strftime('%Y-%m-%dT%H:%M') 
          
          
          #paraAnular_habitacionAnterior_Actualizar(request, contrato)
          
             #-------fuera del horario----------
          if fechaConvertida2.hour <10 or fechaConvertida2.hour>=17:
                messages.error(request, "El horario no corresponde")
                return redirect('Contrato')
           
           
          else:
              
               id_habitacion = contrato.habitacion.id
               habitacion = get_object_or_404(Habitacion, id=id_habitacion)
              # importe_otros_gast= contrato.importe_otros_gasto
               late_check_out = habitacion.check_out_lates
               #importe_estadia = float(contrato.importe_estadia)+ float(late_check_out)
              # total = float(importe_estadia)+ float(importe_otros_gast)
               total =calcularTotal(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
               importeEstadia =calcularImporteEstadia(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
               
               contrato.total=total
          
               contrato.fecha_salida = fechaFormateada2
               contrato.fecha_entrada=fechaFormateada
               contrato.importe_estadia= importeEstadia
               contrato.importe_otros_gasto= importe_otros_gast
               
               
              
               
               try:
                contrato.save()
                #habitacionOcupada(request, habitacions)#acabo de copiar esto de abajo
        
              
                messages.success(request, "El contrato se actualizo correctamente...")
               
                return redirect('modificarContrato')
               
               
               except:
                messages.error(request, "El contrato no se actualizo...")
                return redirect('modificarContrato')
            
              
               
          
     
     
     else:
          
          formContrato = FormContrato(instance=contrato)
          
     
     
     
     
     return render(request, "contrato/modificarTablaContrato.html", {'formContrato': formContrato, 'contrato':contrato, 'habitacion_para_form': habitacion_para_form})


    

def eliminarContrato(request, id_contrato):
     
    contrato = get_object_or_404(Contrato, id=id_contrato)
    nombre = Contrato.habitacion
    
   
   
    #ponerFalse_cuando_elimino(request, id_contrato)
    
    #----------------------agrego esto antes no estaba----------------------------------
    id_habitacion = contrato.habitacion.id
    habitacion = get_object_or_404(Habitacion, id=id_habitacion)
    habitacion.estado="Null"
    habitacion.save()
    
  
    
   
 
  
    
    try:
         contrato.delete()
        
        
         
     
       
         messages.success(request, "El contrato se elimino correctamente...")
         
         
    except:
         messages.error(request, "El contrato no se elimino...")
         
   
         
    return redirect('modificarContrato')



def calcularTotal(request, fecha_entra, fecha_sali, habitacions, importe_otros_gasto):
          contrato = Contrato()
          #total =0
         
     
     
         
          total = contrato.calcularFechas(fecha_entra, fecha_sali, habitacions, importe_otros_gasto)
          
    
     
          return total
     
     
def calcularImporteEstadia(request, fecha_entra, fecha_sali, habitacions, importe_otros_gasto):
          
          contrato = Contrato()
          #total =0
         
     
     
         
          importeEstadia = contrato.calcularImporteEstadia(fecha_entra, fecha_sali, habitacions, importe_otros_gasto)
          
    
     
          return importeEstadia
     
     
     
     
def habitacionOcupada(request, habitacions):
     
    # habitacion=Habitacion()
     
     if request.method == 'POST':
           habitacion = Habitacion.objects.get(id= habitacions)
           habitacion.estado="ocupada"
           
           habitacion.save()
     
     

# def  ponerNull_elimino(request, id_contrato):
#      # esta funcion es para cuando elimino un contrato la habitacion me aparezca Null o sea lista para alquilar
#       contrato = Contrato.objects.get(id= id_contrato)
      
#       id = contrato.habitacion.id
      
#       if request.method == 'GET':
#             habitacion = Habitacion.objects.get(id= id)
#             habitacion.estado="Null"
#             habitacion.save()
            
def habilitar_ocupadas(request, id_habitacion):
     
     contrato = Contrato.objects.all()
     
     False_variable = False
     
     if request.method == 'GET':
            habitacion = Habitacion.objects.get(id= id_habitacion)
            habitacion.estado="Null"
            habitacion.save()
            
            
            #-------------le greguego esto------------------------
            
            for contr in contrato:
                 
                 if contr.habitacion== habitacion:
                      contr.estado= False_variable
                      contr.save()
            return redirect('Panel')
       
       
       

        
      
def ponerFalse_cuando_elimino(request, id_contrato):
      contrato = Contrato.objects.get(id= id_contrato)
     
      id = contrato.habitacion.id
      habitacion = Habitacion.objects.get(id= id)
     
      #------le agrego esto---------------------
     
     
    
   
      #False_variable=False
     
     
      #contrato.estado= False_variable
     # #-------le agreegue esto-----------
      #contrato.habitacion.estado = "Null"
      # #-----------------------------------
      #contrato.save()
     
      #habitacion.estado="Null"
      #habitacion.save()
    
      return redirect('Panel')
 
 
def ponerTrue_alUltimoContrato(request, habitacions):
     contrato=Contrato()
     habitacion = Habitacion.objects.get(id = habitacions)
    
     variableTrue = True
     variableFalse = False
     
     contratos = Contrato.objects.filter(habitacion=habitacion)
     ultimo=list()
     
     habitacion = Habitacion.objects.get(id=habitacions)
    
          
    
     
     for contra in contratos:
          if contra.importe_estadia >0:
               ultimo.append(contra)
              #print("contratos de habitaciones", contratos)
              # print("ultimo contrarto", ultimo[-1])
               if ultimo[-1] == contra.habitacion:
                    contra.estado=variableTrue
                   
                    contra.save()
                    
               else:
                    contra.estado=variableFalse
                  
                    contra.save()
                   
                    
    
def ponerOcupada_ultimaHabitacion(request, habitacions):
      habitacion = Habitacion.objects.get(id=habitacions)
      
      habitacion.estado="ocupada"
      habitacion.save()
     
     
  
              
# def agregarOtrosGastos(request, id_contrato): 
#         #contrato = Contrato()
#      formContrato = FormContrato()
     
#      contrato = get_object_or_404(Contrato, id=id_contrato)
     
    
     
    
     
     
#      #.....................................ahora obtengo el huesped y el contrato mediante el id........................
   
     
#      if request.method == "POST":
        
        
     
          
        
         
      
#           importe_otros_gast= request.POST.get("importe_otros_gasto")
        
          
     
         
#           importe_estadia = float(contrato.importe_estadia)
#           total = float(importe_otros_gast)+float(importe_estadia)
        
#           contrato.importe_otros_gasto= importe_otros_gast
#           contrato.importe_estadia= importe_estadia
#           contrato.total= total
               
#           try:
#                contrato.save()
             
              
#                messages.success(request, "El gasto se agrego correctamente...")
               
#                return redirect('modificarContrato')
               
               
#           except:
#                messages.error(request, "El gasto no se agrego...")
#                return redirect('modificarContrato')
               
               
               
     
     
#      else:
          
#           formContrato = FormContrato()
          
     
     
     
     
#      return render(request, "contrato/agregar_otrosGastos.html", {'formContrato': formContrato, 'contrato':contrato})
            
    
     
    
               
""" def paraAnular_habitacionAnterior_Actualizar(request, contrato):
     contratos = Contrato.objects.all()
     variable=True
     variable2=False
     lista = list()
     id = contrato.id
     contrato = Contrato.objects.get(id=id)
     
     for contra in contratos:
          lista.append(contra.habitacion)
          lista[-1]
          
         
          if  contrato.habitacion != lista[-1]:
               
              contrato.estado=variable2
              contra.save()
          
          else:
                if contrato.habitacion != lista[-1]:
                     contrato.estado= variable2
                     contrato.save()
            
          
                 
               
          """
     
            

           
           
      
     
    
    
    
    
     
     
    
    
    
   
        
           
       
  
          
          
          
     
    
 
    
       
     
       
              
            
              
       
              
     
       
    
    

     
   
   
     
    
    
         
         
     
     
     
     
   
               
     
               
    
     
  
    
    
    







