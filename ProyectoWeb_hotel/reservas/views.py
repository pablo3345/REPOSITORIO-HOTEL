from django.shortcuts import render, redirect, get_object_or_404
from reservas.forms import FormHuesped_reserva, FormReserva
from contrato.formsHuesped import FormHuesped
from reservas.models import HuespedReserva
from django.contrib import messages
import datetime
from habitacion.models import Habitacion
from contrato.models import Contrato, Huesped
from reservas.models import Reserva
from contrato.formsContrtato import FormContrato




# Create your views here.


def mostrar_reserva(request):
    
    
   # FormHuesped_reservas = FormHuesped_reserva()
    FormReservas = FormReserva()
    if request.method =='POST':
         
     formHuesped_reservas =FormHuesped_reserva(request.POST)
         
     if formHuesped_reservas.is_valid():
              
               formHuesped_reservas.save()
               messages.success(request, "El huesped de reserva se guardo correctamente...")
              
     else:
              messages.error(request, "El huesped no se guardo...")
              
     return redirect('mostrar_reservas')
     
    else:
          formHuesped_reservas=FormHuesped_reserva()
          
          
          
     
    
    return render(request, "reservas/reservas.html", {'FormReservas': FormReservas, 'FormHuesped_reservas':formHuesped_reservas})





def guardarReserva(request):
      
     formHuesped_reservas = FormHuesped_reserva()
     formReservas = FormReserva()
     contrato = Contrato()
     
     true_variable = True
     
     reserva=Reserva()
     
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
          
          descuento_porNoche= request.POST.get("descuento_importe_noche")
          descuento_total_importe= request.POST.get("descuento_total_calcularo")
          aumento_Total= request.POST.get("aumento_total")
          
          
          porcentaje_de_senia= request.POST.get("porcentaje_de_senia")
          
          # -----json eliminar-------------------------------------------
        
          
     #.........................cambiar formato calendario.....................
          fechaConvertida = datetime.datetime.strptime(fecha_entra, '%Y-%m-%dT%H:%M') # strptime lo convierto a objeto datetime, el segundo parametro le dice como interpretar la fecha, cual es la hora, el dia, el mes etc
     
          fechaFormateada = fechaConvertida.strftime('%Y-%m-%dT%H:%M') # strftime para darle el formato que quiero
       
        
          fechaConvertida2 = datetime.datetime.strptime(fecha_sali, '%Y-%m-%dT%H:%M')
          fechaFormateada2 = fechaConvertida2.strftime('%Y-%m-%dT%H:%M') 
          
          #habitacion = Habitacion.objects.get(id= habitacions)
          #huesped = Huesped.objects.get(id=huespeds)
          habitacion = get_object_or_404(Habitacion, id=habitacions)
          huesped = get_object_or_404(HuespedReserva, id=huespeds)
          
          #-------------------------id contrato para ponerle True----------------------
          id_contrato = contrato.id
          
          #-------fuera del horario----------
          if fechaConvertida2.hour <10 or fechaConvertida2.hour>=18:
                messages.error(request, "El horario no corresponde")
                return redirect('Contrato')
          
        
          
          
          total =calcularTotal(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
          importeEstadia =contrato.calcularImporteEstadia(fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
          diferenciaConvertida = contrato.nochesDeEstadia(fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
        
           #---------------para sacar la promocion de descuento-------------- pr volver------
         # total_estadia_con_descuento_Late =descuento_delTotal_Promocion_menosLate(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          #total_estadia_con_descuento_diez =descuento_delTotal_Promocion_chekOut_diez(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
           #para volver atras--------------...........----------------------
          
          if int(descuento_porNoche) != 0 and int(descuento_total_importe) != 0:
               
               messages.error(request, "ingreso porcentajes en varias opciones")
               return redirect('Contrato')
          
         # elif  int(descuento_porNoche) != 0 and int(aumento_Total) != 0:
             #   messages.error(request, "ingreso porcentajes en varias opciones")
             #   return redirect('Contrato')
         # elif int(descuento_total_importe) != 0 and int(aumento_Total) != 0:
             #  messages.error(request,"ingreso porcentajes en varias opciones")
              # return redirect('Contrato')
          
          elif int(descuento_total_importe) != 0 and int(aumento_Total) != 0 and int(descuento_porNoche) != 0:
                messages.error(request,"ingreso porcentajes en varias opciones")
                return redirect('Contrato')
          
              
         
          if int(descuento_porNoche) != 0 and int(aumento_Total) ==0:
               messages.success(request, "agrego descuento al precio de la habitacion por cada noche")
               
             
             
               if fechaConvertida2.hour==10 and fechaConvertida2.minute==0:
                     total_estadia_con_descuento_diez =descuento_delTotal_Promocion_chekOut_diez(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                     reserva.importe_estadia= total_estadia_con_descuento_diez
                     reserva.total = total_estadia_con_descuento_diez + float(importe_otros_gast)
                    
                    
               else:
                    if fechaConvertida2.hour >=10 and fechaConvertida2.hour <18:
                          total_estadia_con_descuento_Late =descuento_delTotal_Promocion_menosLate(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                          reserva.importe_estadia= total_estadia_con_descuento_Late
                          reserva.total= total_estadia_con_descuento_Late + float(importe_otros_gast)
                        
                         
                    
                    
          
                     
                     
        
                  
          elif int(aumento_Total) != 0 and  int(descuento_porNoche) == 0 and int(descuento_total_importe)== 0: # esto lo agregue a lo ultimo de la noche
                 reserva.importe_estadia= importeEstadia
                
                 aumento_total = total* float(aumento_Total) /100
                 aumento_total2 = aumento_total
                 reserva.total= total + aumento_total2
             
                 messages.success(request, "agrego un aumento al total del importe")
          
          
          elif  int(descuento_total_importe) !=0  and int(aumento_Total) ==0: # esto lo agregue ahor para volver atras-----
                 reserva.importe_estadia= importeEstadia
                
                 descuentoTotal = total* float(descuento_total_importe) /100
                 descuentoTotal2 = descuentoTotal
                  
               
                 reserva.total= total - descuentoTotal2
                 
               
               
                 messages.success(request, "agrego descuento al total")
                 
         #---------------------------APRETANDO DOS OPCIONES------------------------------- 
         
          elif int(descuento_porNoche) != 0 and int(aumento_Total) != 0:
               reserva.habitacion =habitacion 
          
               reserva.huesped = huesped
               reserva.fecha_entrada= fechaFormateada
               reserva.fecha_salida = fechaFormateada2
          
          #-------------------agregue los descuentos ---------------------
          
               reserva.descuento_importe_noche=descuento_porNoche
               reserva.descuento_total_calcularo=descuento_total_importe
               reserva.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
               reserva.importe_otros_gasto = importe_otros_gast
        
               reserva.estado=true_variable
       
        
         
               messages.success(request, "aplico un descuento por cada noche y un aumento sobre el total")
             #---------------------------para volver atras-------------------
               if fechaConvertida2.hour==10 and fechaConvertida2.minute==0:
                     total_estadia_con_descuento_diez =descuento_delTotal_Promocion_chekOut_diez(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                     reserva.importe_estadia= total_estadia_con_descuento_diez
                     reserva.total = total_estadia_con_descuento_diez + float(importe_otros_gast)
                     
               #-------------aumento-----------    
                     total= reserva.total
                     total2 = total *float(aumento_Total)/100
                     total3 = total +total2
                     
                     reserva.total = total3
                     
                     reserva.total_senia=0
                      
                     reserva.save()
                     
                     
                   
                    
               else:
                    if fechaConvertida2.hour >=10 and fechaConvertida2.hour <18:
                          total_estadia_con_descuento_Late =descuento_delTotal_Promocion_menosLate(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                          reserva.importe_estadia= total_estadia_con_descuento_Late
                          reserva.total= total_estadia_con_descuento_Late + float(importe_otros_gast)
                          
                        
                 
          #---------------------aumento-------------------------------
                  
                      
                    total= reserva.total
                    total2 = total *float(aumento_Total)/100
                    total3 = total +total2
                    
       
                     
                    reserva.total = total3
                    
                    reserva.total_senia=0
                      
                    reserva.save()
                    
                    
          elif  int(descuento_total_importe) !=0  and int(aumento_Total) != 0:
                 reserva.habitacion =habitacion 
          
                 reserva.huesped = huesped
                 reserva.fecha_entrada= fechaFormateada
                 reserva.fecha_salida = fechaFormateada2
          
          #-------------------agregue los descuentos ---------------------
          
                 reserva.descuento_importe_noche=descuento_porNoche
                 reserva.descuento_total_calcularo=descuento_total_importe
                 reserva.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
                 reserva.importe_otros_gasto = importe_otros_gast
        
                 reserva.estado=true_variable
       
                
                 reserva.importe_estadia= importeEstadia
                
                 descuentoTotal = total* float(descuento_total_importe) /100
                 descuentoTotal2 = descuentoTotal
                  
               
                 reserva.total= total - descuentoTotal2
                 
                 #-------le agregue estado y total seña---------------------------
                 reserva.estado= true_variable
                 reserva.total_senia=0
                 #-----------------------------------------------
                 
                 reserva.save()
               
                # messages.success(request, "agrego descuento al total importe")
                 #----------------------------------------
                 
                 total= reserva.importe_estadia
                      
                 #estadia_mas_otros_gastos = float(contrato.importe_estadia)+ float(contrato.importe_otros_gasto)
                 estadia_mas_otros_gastos = float(reserva.importe_estadia)+ float(importe_otros_gast)
                      
                 descuento =estadia_mas_otros_gastos*float(descuento_total_importe)/100
                      
                      
                 tota2 = estadia_mas_otros_gastos- descuento
                      
                 tota2 = tota2 + tota2 *float(aumento_Total)/100
                          
                     
                      
                 reserva.total = tota2
                 
                 messages.success(request, "agrego descuento al total importe, y luego un aumento al total")
                      
                 reserva.save()
                   
                     
                 
         
                
               
               
          
               
               
          else:
               
               
               reserva.importe_estadia= importeEstadia
               reserva.total= total
             
               
          
         
              
                         
               
              
     
          
          reserva.habitacion =habitacion # obtuve la habitacion mediante el id
          
          reserva.huesped = huesped
          reserva.fecha_entrada= fechaFormateada
          reserva.fecha_salida = fechaFormateada2
          
          #-------------------agregue los descuentos ---------------------
          
          reserva.descuento_importe_noche=descuento_porNoche
          reserva.descuento_total_calcularo=descuento_total_importe
          reserva.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
          reserva.importe_otros_gasto = importe_otros_gast
        
          reserva.estado=true_variable
          
          reserva.total_senia=0
          
          reserva.porcentaje_de_senia= porcentaje_de_senia
       
        
         
          
               
          
          
         #----para---------volver------------
          try:
          
           
        
           #ponerTrue_alUltimoContrato(request, habitacions)
          # ponerOcupada_ultimaHabitacion(request, habitacions)
          
           
          
           reserva.save()
          
           
          
         
               
               
           
           
          
        
           messages.success(request, "La reserva se guardo correctamente...")
          
               
            
           
           
          except:
               messages.error(request, "La reserva no se guardo...")
               
               
        
             
                    
      
             
          
     else:
         form2 = FormReserva()
     
     
     
     return render(request, "reservas/reservas.html", {'FormReservas': formReservas, 'FormHuesped_reservas':formHuesped_reservas, 'total': total, 'importe_de_otros_gastos':importe_otros_gast, 'importe_estadia':importeEstadia, 'diferenciaConvertida':diferenciaConvertida, 'descuento':descuento_porNoche, 'descuento_total': descuento_total_importe, 'aumento':aumento_Total})
     
     

def descuento_delTotal_Promocion_menosLate(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast):
          contrato= Contrato()
          
          
     
          habitacions = request.POST.get("habitacion")
          
          habitacion = get_object_or_404(Habitacion, id=habitacions)
          
         # habitacion = Habitacion.objects.get(id = habitacions)
        
          fecha_entra = request.POST.get("fecha_entrada")
          fecha_sali = request.POST.get("fecha_salida")
         
          importe_otros_gast= request.POST.get("importe_otros_gasto")
          
          descuento= request.POST.get("descuento_importe_noche")
          # descuento= request.POST.get("descuento")
        
         
     
          importeEstadia =contrato.calcularImporteEstadia(fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          diferenciaConvertida = contrato.nochesDeEstadia(fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
         
          
          retas1 = importeEstadia 
          
          resta2 = retas1- float(habitacion.check_out_lates)
          
          resta3 = resta2 / diferenciaConvertida
          
          #..................aca tengo el precio por noche de la habitacion-----------
          
          total1 = resta3 * int(descuento) /100
          #..................................................
          total2 = diferenciaConvertida*total1
          
          #----------------------------------------------
          
          total_con_descuento = importeEstadia - total2
          
          #------------le agrego el late check aut---------------------
          
          
          
          
          
          
          return total_con_descuento # este seria el importe de estadia NO  el total

          

def descuento_delTotal_Promocion_chekOut_diez(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast):
          contrato= Contrato()
          
         
          
     
          habitacions = request.POST.get("habitacion")
          
         # habitacion = Habitacion.objects.get(id = habitacions)
          habitacion = get_object_or_404(Habitacion, id=habitacions)
        
          fecha_entra = request.POST.get("fecha_entrada")
          fecha_sali = request.POST.get("fecha_salida")
         
          importe_otros_gast= request.POST.get("importe_otros_gasto")
          
          #descuento= request.POST.get("descuento")
          descuento= request.POST.get("descuento_importe_noche")
          
        

     
          importeEstadia =contrato.calcularImporteEstadia(fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          diferenciaConvertida = contrato.nochesDeEstadia(fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
        
          
          retas1 = importeEstadia 
          
          resta2 = retas1
          
          resta3 = resta2 / diferenciaConvertida
          
          #..................aca tengo el precio por noche de la habitacion-----------
          #para volver-------------------------------------
          
          total1 = resta3 * int(descuento) /100
          #..................................................
          total2 = diferenciaConvertida*total1
          
          #----------------------------------------------
          
          total_con_descuento = importeEstadia - total2
          
          
          
          return total_con_descuento # este seria el importe de estadia NO  el total

          
def calcularTotal(request, fecha_entra, fecha_sali, habitacions, importe_otros_gasto):
          contrato = Contrato()
          #total =0
         
     
     
         
          total = contrato.calcularFechas(fecha_entra, fecha_sali, habitacions, importe_otros_gasto)
          
    
     
          return total
    
    
def modificarReservas(request):
      
      reservas = Reserva.objects.all()
      
      
      
      return render(request, "reservas/modificarReservas.html", {'reservas': reservas})




def enviar_a_contrato(request, id_reserva):
      
      form1 = FormContrato()
      form2 = FormHuesped()
   #----------------------------huesped-----------------------------------   
      huesped=Huesped()
      contrato=Contrato()
      
      reserva =  get_object_or_404(Reserva, id=id_reserva)
      
      id_huesped = reserva.huesped.id
      
      huesped_reserva =  get_object_or_404(HuespedReserva, id=id_huesped)
      
     
        
    
        
    
          
      huesped.nombre_responsable= huesped_reserva.nombre
      huesped.apellido= huesped_reserva.apellido
      huesped.dni = huesped_reserva.dni
      huesped.telefono = huesped_reserva.telefono
      
  #----------------------contrato-----------------------------------------------
      contrato.habitacion= reserva.habitacion
      contrato.fecha_entrada= str(reserva.fecha_entrada)
      contrato.fecha_salida= str(reserva.fecha_salida)
      contrato.importe_otros_gasto= reserva.importe_otros_gasto
      contrato.descuento_importe_noche= reserva.descuento_importe_noche
      contrato.descuento_total_calcularo= reserva.descuento_total_calcularo
      contrato.aumento_total = reserva.aumento_total
      
      
     
      
      guardarHuesped(request)
     
     
      
          
         
     
     
      form2 = FormHuesped(instance=huesped)
      
      form1= FormContrato(instance=contrato)
      
      
    
     
          
      
      
      
      
      
      return render(request, "reservas/enviar_a_contrato.html", {'formHuesped': form2, 'formContrato': form1})
      
      
      
      
def guardarHuesped(request):
      
     huesped = Huesped()
      
     nombre_resp = request.POST.get("nombre_responsable")
     apelli = request.POST.get("apellido")
     edadd = request.POST.get("edad")
     dnii = request.POST.get("dni")
     demas_huespe = request.POST.get("demas_huespedes")
     patente_vehicu = request.POST.get("patente_vehiculo")
     modelo_vehicu = request.POST.get("modelo_vehiculo")
     correo_electro =request.POST.get("correo_electronico")
     #----------------------------------------------------------
     direccion= request.POST.get("direccion")
     localidad = request.POST.get("localidad")
     codigo_postal =  request.POST.get("codigo_postal")
     pais= request.POST.get("pais")
     telefono= request.POST.get("telefono")
     if request.method =='POST':
          
          huesped.nombre_responsable= nombre_resp
          huesped.apellido = apelli
          huesped.edad = edadd
          huesped.dni = dnii
          huesped.demas_huespedes = demas_huespe
          huesped.patente_vehiculo= patente_vehicu
          huesped.modelo_vehiculo= modelo_vehicu
          huesped.correo_electronico= correo_electro
          #---------------------------------------
          huesped.direccion= direccion
          huesped.localidad= localidad
          huesped.codigo_postal= codigo_postal
          huesped.pais=pais
          huesped.telefono= telefono
          
         
          
         
          try:
                
           huesped.save()
           messages.success(request, "El huesped se guardo correctamente...")
           
          except:
                 messages.error(request, "El huesped no se guardo...")
                 
         # return redirect('guardarReserva')
                 
    
          
          
       