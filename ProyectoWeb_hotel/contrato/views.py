from django.shortcuts import render, redirect, get_object_or_404
from contrato.formsContrtato import FormContrato 
from contrato.formsHuesped import FormHuesped
from django.contrib import messages
from contrato.models import Huesped, Contrato
import datetime
from habitacion.models import Habitacion


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
        # contrato.late_chack_out = late_check_out #lo agregue nuevo
          contrato.total = total 
          
          """  if total==0:
               return redirect("Inicio")
           """
          
          
               
          
          
         
          try:
          
           
        
               
           print("el total es total", total)
           contrato.save()
           messages.success(request, "El contrato se guardo correctamente...")
          
               
            
           
           
          except:
               messages.error(request, "El contrato no se guardo...")
               
               
        
             
                    
      
             
          
     else:
         form2 = FormContrato()
     
     
     
     return render(request, "contrato/contrato.html", {'formHuesped': form, 'formContrato': form2, 'total': total, 'importe_de_otros_gastos':importe_otros_gast, 'importe_estadia':importeEstadia, 'diferenciaConvertida':diferenciaConvertida})
     
     
   
               
              
             
def modificarContrato(request):
          
     contratos = Contrato.objects.all()
     
     return render(request, "contrato/modificarContrato.html",{'contratos': contratos})  



def modificarTablaContrato(request, id_contrato):
     contrato = Contrato()
     formContrato = FormContrato()
     contrato = get_object_or_404(Contrato, id=id_contrato)
     
     habitacions = request.POST.get("habitacion")# id
     huespeds =request.POST.get("huesped")# id
     
     fecha_entra = request.POST.get("fecha_entrada")
     fecha_sali = request.POST.get("fecha_salida")
    # importe_estad= request.POST.get("importe_estadia")
     importe_otros_gast= request.POST.get("importe_otros_gasto")
    # late_check_out = request.POST.get("late_chack_out")
     #totals= request.POST.get("total")
    
     
     
     #.....................................ahora obtengo el huesped y el contrato mediante el id........................
   
     
     if request.method == "POST":
          habitacion = Habitacion.objects.get(id= habitacions)
          huesped = Huesped.objects.get(id=huespeds)
          
          total =calcularTotal(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
          importeEstadia =calcularImporteEstadia(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
          
          
          
          
          contrato.habitacion = habitacion
          contrato.huesped = huesped
          contrato.fecha_entrada = fecha_entra
          contrato.fecha_salida = fecha_sali
          contrato.importe_estadia= importeEstadia
          contrato.importe_otros_gasto = importe_otros_gast
         # contrato.late_chack_out= late_check_out
          contrato.total=total
          
          try:
               contrato.save()
               messages.success(request, "El contrato se actualizo correctamente...")
               return redirect('modificarContrato')
               
               
          except:
               messages.error(request, "El contrato no se actualizo...")
               return redirect('modificarContrato')
               
               
     
     
     
     
     else:
          
          formContrato = FormContrato(instance=contrato)
          
     
     
     
     
     return render(request, "contrato/modificarTablaContrato.html", {'formContrato': formContrato})


def eliminarContrato(request, id_contrato):
     
    contrato = get_object_or_404(Contrato, id=id_contrato)
    
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
     
     

     
     
        
        
     
   
        
           
       
  
          
          
          
     
    
 
    
       
     
       
              
            
              
       
              
     
       
    
    

     
   
   
     
    
    
         
         
     
     
     
     
   
               
     
               
    
     
  
    
    
    







