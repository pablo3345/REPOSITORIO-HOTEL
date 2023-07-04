from django.shortcuts import render, redirect, get_object_or_404
from contrato.formsContrtato import FormContrato 
from contrato.formsHuesped import FormHuesped
from django.contrib import messages
from contrato.models import Huesped, Contrato
import datetime
from habitacion.models import Habitacion
from panel_de_admin.views import mostrarPanel
from django.views.generic import View
from .utilitario import render_to_pdf
from django.http import HttpResponse

#import json


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
     #----------------------------------------------------------
     direccion= request.POST.get("direccion")
     localidad = request.POST.get("localidad")
     codigo_postal =  request.POST.get("codigo_postal")
     pais= request.POST.get("pais")
     
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
          
          descuento_porNoche= request.POST.get("descuento_importe_noche")
          descuento_total_importe= request.POST.get("descuento_total_calcularo")
          aumento_Total= request.POST.get("aumento_total")
          
     #.........................cambiar formato calendario.....................
          fechaConvertida = datetime.datetime.strptime(fecha_entra, '%Y-%m-%dT%H:%M') # strptime lo convierto a objeto datetime, el segundo parametro le dice como interpretar la fecha, cual es la hora, el dia, el mes etc
     
          fechaFormateada = fechaConvertida.strftime('%Y-%m-%dT%H:%M') # strftime para darle el formato que quiero
       
        
          fechaConvertida2 = datetime.datetime.strptime(fecha_sali, '%Y-%m-%dT%H:%M')
          fechaFormateada2 = fechaConvertida2.strftime('%Y-%m-%dT%H:%M') 
          
          #habitacion = Habitacion.objects.get(id= habitacions)
          #huesped = Huesped.objects.get(id=huespeds)
          habitacion = get_object_or_404(Habitacion, id=habitacions)
          huesped = get_object_or_404(Huesped, id=huespeds)
          
          #-------------------------id contrato para ponerle True----------------------
          id_contrato = contrato.id
          
          #-------fuera del horario----------
          if fechaConvertida2.hour <10 or fechaConvertida2.hour>=18:
                messages.error(request, "El horario no corresponde")
                return redirect('Contrato')
          
        
          
          
          total =calcularTotal(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
          importeEstadia =calcularImporteEstadia(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
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
                     contrato.importe_estadia= total_estadia_con_descuento_diez
                     contrato.total = total_estadia_con_descuento_diez + float(importe_otros_gast)
                    
                    
               else:
                    if fechaConvertida2.hour >=10 and fechaConvertida2.hour <18:
                          total_estadia_con_descuento_Late =descuento_delTotal_Promocion_menosLate(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                          contrato.importe_estadia= total_estadia_con_descuento_Late
                          contrato.total= total_estadia_con_descuento_Late + float(importe_otros_gast)
                        
                         
                    
                    
          
                     
                     
        
                  
          elif int(aumento_Total) != 0 and  int(descuento_porNoche) == 0 and int(descuento_total_importe)== 0: # esto lo agregue a lo ultimo de la noche
                 contrato.importe_estadia= importeEstadia
                
                 aumento_total = total* float(aumento_Total) /100
                 aumento_total2 = aumento_total
                 contrato.total= total + aumento_total2
             
                 messages.success(request, "agrego un aumento al total del importe")
          
          
          elif  int(descuento_total_importe) !=0  and int(aumento_Total) ==0: # esto lo agregue ahor para volver atras-----
                 contrato.importe_estadia= importeEstadia
                
                 descuentoTotal = total* float(descuento_total_importe) /100
                 descuentoTotal2 = descuentoTotal
                  
               
                 contrato.total= total - descuentoTotal2
                 
               
               
                 messages.success(request, "agrego descuento al total")
                 
         #---------------------------APRETANDO DOS OPCIONES------------------------------- 
         
          elif int(descuento_porNoche) != 0 and int(aumento_Total) != 0:
               contrato.habitacion =habitacion 
          
               contrato.huesped = huesped
               contrato.fecha_entrada= fechaFormateada
               contrato.fecha_salida = fechaFormateada2
          
          #-------------------agregue los descuentos ---------------------
          
               contrato.descuento_importe_noche=descuento_porNoche
               contrato.descuento_total_calcularo=descuento_total_importe
               contrato.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
               contrato.importe_otros_gasto = importe_otros_gast
        
               contrato.estado=true_variable
       
        
         
               messages.success(request, "aplico un descuento por cada noche y un aumento sobre el total")
             #---------------------------para volver atras-------------------
               if fechaConvertida2.hour==10 and fechaConvertida2.minute==0:
                     total_estadia_con_descuento_diez =descuento_delTotal_Promocion_chekOut_diez(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                     contrato.importe_estadia= total_estadia_con_descuento_diez
                     contrato.total = total_estadia_con_descuento_diez + float(importe_otros_gast)
                     
               #-------------aumento-----------    
                     total= contrato.total
                     total2 = total *float(aumento_Total)/100
                     total3 = total +total2
                     
                     contrato.total = total3
                      
                     contrato.save()
                   
                    
               else:
                    if fechaConvertida2.hour >=10 and fechaConvertida2.hour <18:
                          total_estadia_con_descuento_Late =descuento_delTotal_Promocion_menosLate(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                          contrato.importe_estadia= total_estadia_con_descuento_Late
                          contrato.total= total_estadia_con_descuento_Late + float(importe_otros_gast)
                          
                        
                 
          #---------------------aumento-------------------------------
                  
                      
                    total= contrato.total
                    total2 = total *float(aumento_Total)/100
                    total3 = total +total2
                    
       
                     
                    contrato.total = total3
                      
                    contrato.save()
                    
                    
          elif  int(descuento_total_importe) !=0  and int(aumento_Total) != 0:
                 contrato.habitacion =habitacion 
          
                 contrato.huesped = huesped
                 contrato.fecha_entrada= fechaFormateada
                 contrato.fecha_salida = fechaFormateada2
          
          #-------------------agregue los descuentos ---------------------
          
                 contrato.descuento_importe_noche=descuento_porNoche
                 contrato.descuento_total_calcularo=descuento_total_importe
                 contrato.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
                 contrato.importe_otros_gasto = importe_otros_gast
        
                 contrato.estado=true_variable
       
                
                 contrato.importe_estadia= importeEstadia
                
                 descuentoTotal = total* float(descuento_total_importe) /100
                 descuentoTotal2 = descuentoTotal
                  
               
                 contrato.total= total - descuentoTotal2
                 
                 contrato.save()
               
                # messages.success(request, "agrego descuento al total importe")
                 #----------------------------------------
                 
                 total= contrato.importe_estadia
                      
                 estadia_mas_otros_gastos = float(contrato.importe_estadia)+ float(contrato.importe_otros_gasto)
                      
                 descuento =estadia_mas_otros_gastos*float(descuento_total_importe)/100
                      
                      
                 tota2 = estadia_mas_otros_gastos- descuento
                      
                 tota2 = tota2 + tota2 *float(aumento_Total)/100
                          
                     
                      
                 contrato.total = tota2
                 
                 messages.success(request, "agrego descuento al total importe, y luego un aumento al total")
                      
                 contrato.save()
                   
                     
                 
         
                
               
               
          
               
               
          else:
               
               
               contrato.importe_estadia= importeEstadia
               contrato.total= total
             
               
          
         
              
                         
               
              
     
          
          contrato.habitacion =habitacion # obtuve la habitacion mediante el id
          
          contrato.huesped = huesped
          contrato.fecha_entrada= fechaFormateada
          contrato.fecha_salida = fechaFormateada2
          
          #-------------------agregue los descuentos ---------------------
          
          contrato.descuento_importe_noche=descuento_porNoche
          contrato.descuento_total_calcularo=descuento_total_importe
          contrato.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
          contrato.importe_otros_gasto = importe_otros_gast
        
          contrato.estado=true_variable
       
        
         
          
               
          
          
         
          try:
          
           
        
           ponerTrue_alUltimoContrato(request, habitacions)
           ponerOcupada_ultimaHabitacion(request, habitacions)
          
           
          
           contrato.save()
          
           
          
           """  if int(aumento_Total) != 0 and int(descuento_total_importe) != 0: # le agregue  and descuento_total_importe==0:
                 contrato.importe_estadia= importeEstadia
                
                 descuentoTotal = total* float(descuento_total_importe) /100
                 descuentoTotal2 = descuentoTotal
                  
               
                 contrato.total= total - descuentoTotal2
                 
                 contrato.save()
               
                 messages.success(request, "agrego descuento al total importe")
                 #----------------------------------------
                 
                 total= contrato.importe_estadia
                      
                 estadia_mas_otros_gastos = float(contrato.importe_estadia)+ float(contrato.importe_otros_gasto)
                      
                 descuento =estadia_mas_otros_gastos*float(descuento_total_importe)/100
                      
                      
                 tota2 = estadia_mas_otros_gastos- descuento
                      
                 tota2 = tota2 + tota2 *float(aumento_Total)/100
                          
                     
                      
                 contrato.total = tota2
                 
                 messages.success(request, "agrego aumento al total importe")
                      
                 contrato.save()
                     
               #--------------------------------------lo traje de arriba---------------------------
           elif int(aumento_Total) != 0 and int(descuento_porNoche) !=0:
                 
                   if fechaConvertida2.hour==10 and fechaConvertida2.minute==0:
                     total_estadia_con_descuento_diez =descuento_delTotal_Promocion_chekOut_diez(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                     contrato.importe_estadia= total_estadia_con_descuento_diez
                     contrato.total = total_estadia_con_descuento_diez + float(importe_otros_gast)
                    
                    
                   else:
                    if fechaConvertida2.hour >=10 and fechaConvertida2.hour <18:
                          total_estadia_con_descuento_Late =descuento_delTotal_Promocion_menosLate(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                          contrato.importe_estadia= total_estadia_con_descuento_Late
                          contrato.total= total_estadia_con_descuento_Late + float(importe_otros_gast)
                        
                         
                    
                
          #---------------------aumento-------------------------------
                   contrato.importe_estadia= importeEstadia
                      
                   total= contrato.importe_estadia
                      
                   estadia_mas_otros_gastos = float(contrato.importe_estadia)+ float(contrato.importe_otros_gasto)
                      
                  # descuento =estadia_mas_otros_gastos*float(descuento_total_importe)/100
                      
                      
                   #tota2 = estadia_mas_otros_gastos- descuento
                      
                   tota2 = estadia_mas_otros_gastos  *float(aumento_Total)/100
                   
                   total3 = estadia_mas_otros_gastos+tota2
                          
                     
                   contrato.total = total3
                      
                   contrato.save()
                   messages.success(request, "agrego un aumento total") """
               
                
                
                
                
               #  elif int(aumento_Total) !=0:
                  
               #        contrato.importe_estadia= importeEstadia
                
               #       #--------para volver atras --------------------------
                      
               #        total= contrato.importe_estadia
                      
               #        estadia_mas_otros_gastos = float(contrato.importe_estadia)+ float(contrato.importe_otros_gasto)
                      
               #        descuento =estadia_mas_otros_gastos*float(descuento_total_importe)/100
                      
                      
               #        tota2 = estadia_mas_otros_gastos- descuento
                      
               #        tota2 = tota2 + tota2 *float(aumento_Total)/100
                          
                     
               #        contrato.total = tota2
                      
               #        contrato.save()
               #        messages.success(request, "agrego un descuento y un aumento al total")
               
                     
         
               
               
           
           
          
        
           messages.success(request, "El contrato se guardo correctamente...")
          
               
            
           
           
          except:
               messages.error(request, "El contrato no se guardo...")
               
               
        
             
                    
      
             
          
     else:
         form2 = FormContrato()
     
     
     
     return render(request, "contrato/contrato.html", {'formHuesped': form, 'formContrato': form2, 'total': total, 'importe_de_otros_gastos':importe_otros_gast, 'importe_estadia':importeEstadia, 'diferenciaConvertida':diferenciaConvertida, 'descuento':descuento_porNoche, 'descuento_total': descuento_total_importe, 'aumento':aumento_Total})
     
     
   
               
              
             
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
          
          #---------------------------------
          huespeds =request.POST.get("huesped")# id
          #--------------------------------------------------------
          
          huesped = Huesped.objects.get(id= huespeds)
          
          
          descuento_porNoche= request.POST.get("descuento_importe_noche")
          descuento_total_importe= request.POST.get("descuento_total_calcularo")
          aumento_Total= request.POST.get("aumento_total")
          
          
          
          #-------------------------------------------------------------
          
          true_variable = True
          
          
     
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
          
          #---------------------para volver atras------------
          
        
          fechaConvertida = datetime.datetime.strptime(fecha_entra, '%Y-%m-%dT%H:%M')
     
          fechaConvertida2 = datetime.datetime.strptime(fecha_sali, '%Y-%m-%dT%H:%M')
          fechaFormateada2 = fechaConvertida2.strftime('%Y-%m-%dT%H:%M') 
          
          fechaFormateada = fechaConvertida.strftime('%Y-%m-%dT%H:%M') 
          
          
          #paraAnular_habitacionAnterior_Actualizar(request, contrato)
          total =calcularTotal(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
          importeEstadia =calcularImporteEstadia(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
          diferenciaConvertida = contrato.nochesDeEstadia(fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
          
             #-------fuera del horario----------
          if fechaConvertida2.hour <10 or fechaConvertida2.hour>=18:
                messages.error(request, "El horario no corresponde")
                return redirect('Contrato')
           
           
           
           
           
          else:
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
                     total_estadia_con_descuento_diez =descuento_delTotal_Promocion_chekOut_diez_actualizar_tabla(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                     contrato.importe_estadia= total_estadia_con_descuento_diez
                     contrato.total = total_estadia_con_descuento_diez + float(importe_otros_gast)
                    
                    
                else:
                    if fechaConvertida2.hour >=10 and fechaConvertida2.hour <18:
                          total_estadia_con_descuento_Late =descuento_delTotal_Promocion_menosLate_actualizarTabla(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                          contrato.importe_estadia= total_estadia_con_descuento_Late
                          contrato.total= total_estadia_con_descuento_Late + float(importe_otros_gast)
                        
                         
                    
                   
          
                     
                     
        
                  
               elif int(aumento_Total) != 0 and  int(descuento_porNoche) == 0 and int(descuento_total_importe)== 0: # esto lo agregue a lo ultimo de la noche
                 contrato.importe_estadia= importeEstadia
                
                 aumento_total = total* float(aumento_Total) /100
                 aumento_total2 = aumento_total
                 contrato.total= total + aumento_total2
             
                 messages.success(request, "agrego un aumento al total del importe")
          
          
               elif  int(descuento_total_importe) !=0  and int(aumento_Total) ==0: # esto lo agregue ahor para volver atras-----
                 contrato.importe_estadia= importeEstadia
                
                 descuentoTotal = total* float(descuento_total_importe) /100
                 descuentoTotal2 = descuentoTotal
                  
               
                 contrato.total= total - descuentoTotal2
                 
               
               
                 messages.success(request, "agrego descuento al total")
                 
         #---------------------------APRETANDO DOS OPCIONES------------------------------- 
         
               elif int(descuento_porNoche) != 0 and int(aumento_Total) != 0:
                contrato.habitacion =habitacion 
          
                contrato.huesped = huesped
                contrato.fecha_entrada= fechaFormateada
                contrato.fecha_salida = fechaFormateada2
          
          #-------------------agregue los descuentos ---------------------
          
                contrato.descuento_importe_noche=descuento_porNoche
                contrato.descuento_total_calcularo=descuento_total_importe
                contrato.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
                contrato.importe_otros_gasto = importe_otros_gast
        
                contrato.estado=true_variable
       
        
         
                messages.success(request, "aplico un descuento por cada noche y un aumento sobre el total")
             #---------------------------para volver atras-------------------
                if fechaConvertida2.hour==10 and fechaConvertida2.minute==0:
                     total_estadia_con_descuento_diez =descuento_delTotal_Promocion_chekOut_diez_actualizar_tabla(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                     contrato.importe_estadia= total_estadia_con_descuento_diez
                     contrato.total = total_estadia_con_descuento_diez + float(importe_otros_gast)
                     
               #-------------aumento-----------    
                     total= contrato.total
                     total2 = total *float(aumento_Total)/100
                     total3 = total +total2
                     
                     contrato.total = total3
                      
                     contrato.save()
                   
                    
                else:
                    if fechaConvertida2.hour >=10 and fechaConvertida2.hour <18:
                          total_estadia_con_descuento_Late =descuento_delTotal_Promocion_menosLate_actualizarTabla(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
                          contrato.importe_estadia= total_estadia_con_descuento_Late
                          contrato.total= total_estadia_con_descuento_Late + float(importe_otros_gast)
                          
                        
                 
          #---------------------aumento-------------------------------
                  
                      
                    total= contrato.total
                    total2 = total *float(aumento_Total)/100
                    total3 = total +total2
                    
       
                     
                    contrato.total = total3
                      
                    contrato.save()
                    
                    
               elif  int(descuento_total_importe) !=0  and int(aumento_Total) != 0:
                 contrato.habitacion =habitacion 
          
                 contrato.huesped = huesped
                 contrato.fecha_entrada= fechaFormateada
                 contrato.fecha_salida = fechaFormateada2
          
          #-------------------agregue los descuentos ---------------------
          
                 contrato.descuento_importe_noche=descuento_porNoche
                 contrato.descuento_total_calcularo=descuento_total_importe
                 contrato.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
                 contrato.importe_otros_gasto = importe_otros_gast
        
                 contrato.estado=true_variable
       
                
                 contrato.importe_estadia= importeEstadia
                
                 descuentoTotal = total* float(descuento_total_importe) /100
                 descuentoTotal2 = descuentoTotal
                  
               
                 contrato.total= total - descuentoTotal2
                 
                 contrato.save()
               
                # messages.success(request, "agrego descuento al total importe")
                 #----------------------------------------
                 
                 total= contrato.importe_estadia
                      
                 estadia_mas_otros_gastos = float(contrato.importe_estadia)+ float(contrato.importe_otros_gasto)
                      
                 descuento =estadia_mas_otros_gastos*float(descuento_total_importe)/100
                      
                      
                 tota2 = estadia_mas_otros_gastos- descuento
                      
                 tota2 = tota2 + tota2 *float(aumento_Total)/100
                          
                     
                      
                 contrato.total = tota2
                 
                 messages.success(request, "agrego descuento al total importe, y luego un aumento al total")
                      
                 contrato.save()
                   
                     
                 
         
                
               
               
          
               
               
               else:
               
               
                contrato.importe_estadia= importeEstadia
                contrato.total= total
             
               
          
         
              
                         
               
              
               
               
               
               #------------------------------------------------------------------------
              
               id_habitacion = contrato.habitacion.id
               habitacion = get_object_or_404(Habitacion, id=id_habitacion)
              # importe_otros_gast= contrato.importe_otros_gasto
               late_check_out = habitacion.check_out_lates
               #importe_estadia = float(contrato.importe_estadia)+ float(late_check_out)
              # total = float(importe_estadia)+ float(importe_otros_gast)
               total =calcularTotal(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
          
               importeEstadia =calcularImporteEstadia(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
               
               
                #---------------------volver atras y desbloquera lo de abajo---------------------
               contrato.habitacion =habitacion # obtuve la habitacion mediante el id
          
               contrato.huesped = huesped
               contrato.fecha_entrada= fechaFormateada
               contrato.fecha_salida = fechaFormateada2
          
                #-------------------agregue los descuentos ---------------------
          
               contrato.descuento_importe_noche=descuento_porNoche
               contrato.descuento_total_calcularo=descuento_total_importe
               contrato.aumento_total= aumento_Total
          
         #----------------------------------------------------------- 
       
               contrato.importe_otros_gasto = importe_otros_gast
        
               contrato.estado=true_variable
       
               
               """ contrato.total=total
          
               contrato.fecha_salida = fechaFormateada2
               contrato.fecha_entrada=fechaFormateada
               contrato.importe_estadia= importeEstadia
               contrato.importe_otros_gasto= importe_otros_gast
               #---------------agregue el huesped-----------------
               contrato.huesped=huesped
               
                #-------------------agregue los descuentos ---------------------
          
               contrato.descuento_importe_noche=descuento_porNoche
               contrato.descuento_total_calcularo=descuento_total_importe
               contrato.aumento_total= aumento_Total
           """
               #----------------------------------------------------------- 
               
               #-----------------S--para volver atras-----------------------
               
              
               
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
           # habitacion = Habitacion.objects.get(id= id_habitacion)
            habitacion = get_object_or_404(Habitacion, id=id_habitacion)

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
      
      
def lateCheckout(request, id_contrato):
     formContrato=FormContrato()
     
     #-----para volver atras ----------------
     
     
     
     
    # contrato = Contrato.objects.get(id= id_contrato)
     contrato = get_object_or_404(Contrato, id=id_contrato)
     
      #-----para volver atras -------------------
   
     
     fecha_entra = contrato.fecha_entrada
     fechaFormateada = fecha_entra.strftime('%Y-%m-%dT%H:%M') 
     habitacions = contrato.habitacion.id
     importe_otros_gast= contrato.importe_otros_gasto
     
     
     
     
     if request.method == "POST":
          fecha_sali = request.POST.get("fecha_salida")
          fechaConvertida2 = datetime.datetime.strptime(fecha_sali, '%Y-%m-%dT%H:%M')
        
     
          
          if fechaConvertida2.hour <10 or fechaConvertida2.hour>=18:
                messages.error(request, "El horario no corresponde")
                return redirect('modificarContrato')
          
          
          elif  fechaConvertida2.hour ==10 or fechaConvertida2.minute==0:
               messages.error(request, "El horario no corresponde al late check out")
               return redirect('modificarContrato')
          
          elif fechaConvertida2.day != contrato.fecha_salida.day:
               messages.error(request, "El dia no corresponde al late check out")
               return redirect('modificarContrato')
          
          
          #------- agrego esto para ver que pasa----------------y para volver atras-----
          
        
          
          
          
          
          
          else:
              
               
              
               fechaFormateada2 = fechaConvertida2.strftime('%Y-%m-%dT%H:%M') 
               total =calcularTotal(request, fechaFormateada, fecha_sali, habitacions, importe_otros_gast)
          
               importeEstadia =calcularImporteEstadia(request, fechaFormateada, fecha_sali, habitacions, importe_otros_gast)
     
               contrato.importe_estadia= importeEstadia
               contrato.total= total
               contrato.fecha_salida= fechaFormateada2
               try:
                    
                    
                  contrato.save()
                  messages.success(request, "El late check out se agrego correctamente...")
                  return redirect('modificarContrato')
                    
               except:
                    
                  messages.error(request, "El late check out no se agrego...")
                  return redirect('modificarContrato')
                    
           
          
          
          
     
     
     
     return render(request, "contrato/late_check.html", {'contrato': contrato, 'formContrato': formContrato})
     
     
  
def contratosTotales(request):
     
     contratos = Contrato.objects.all()  
     
     return render(request, 'contrato/tablaContratos_totales.html', {'contratos':contratos})   




class generar_reporter_huespedes(View):
     
   
   
     
     def get(self, request, *args, **kwargs): # **kwargs es un diccionario de argumentos por si les paso
         
          id=self.kwargs.get("id") # lo reconoce como id a los dos nombres, pongo id_huesped y no funciona
       
          huespedes = Huesped.objects.all()
          huesped = get_object_or_404(Huesped, id=id)
          fecha = huesped.created
          
          template_name= "contrato/reporter_huesped.html"
          
          data={'cantidad': huespedes.count(), # a count() es solo un ejemplo no lo voy a usar
                'huespedes': huespedes,
                'huesped': huesped,
                'fecha': fecha
                
              
             
              
                
                } # count es para saber la cantidad de objetos que tiene el modelo huesped
          
          pdf = render_to_pdf(template_name, data) # aca le mando el template y el contenido(contexto, diccionario) a la funcion de utulitario donde me convierte el template a pdf
          
          return HttpResponse(pdf, content_type= 'application/pdf' )
     
     
     
def cambiar_total(request, id_contrato):
     
     contrato = get_object_or_404(Contrato, id=id_contrato)
   
     data={
          'habitacion': contrato.habitacion,
          'huesped': contrato.huesped,
          'fecha_entrada': contrato.fecha_entrada,
          'fecha_salida': contrato.fecha_salida,
          'total_anterior': contrato.total
          
     }
     
     if request.method == "POST":
          total_cambiado = request.POST.get("cambiar_total")
          contrato.total= total_cambiado
          try:
           contrato.save()
           messages.success(request, "El total se actualizo correctamente...")
           
          except:
               messages.error(request, "El total no se actualizo...")
          return redirect('modificarContrato')
     
     
     return render(request, "contrato/cambiar_total.html", {'data': data})





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
        
         
     
          importeEstadia =calcularImporteEstadia(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
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
          
        

     
          importeEstadia =calcularImporteEstadia(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
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

          
          
#----------para volver atras -------------PARA DESCUENTO POR NOCHE EN ACTUALIZAR TABLA-------------------
def descuento_delTotal_Promocion_menosLate_actualizarTabla(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast):
          contrato= Contrato()
          
          
     
          #habitacions = request.POST.get("habitacion")
          
          habitacion = get_object_or_404(Habitacion, id=habitacions)
          
         # habitacion = Habitacion.objects.get(id = habitacions)
        
          fecha_entra = request.POST.get("fecha_entrada")
          fecha_sali = request.POST.get("fecha_salida")
         
          importe_otros_gast= request.POST.get("importe_otros_gasto")
          
          descuento= request.POST.get("descuento_importe_noche")
          # descuento= request.POST.get("descuento")
        
         
     
          importeEstadia =calcularImporteEstadia(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
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



def descuento_delTotal_Promocion_chekOut_diez_actualizar_tabla(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast):
          contrato= Contrato()
          
         
          
     
         #habitacions = request.POST.get("habitacion")
          
         # habitacion = Habitacion.objects.get(id = habitacions)
          habitacion = get_object_or_404(Habitacion, id=habitacions)
        
          fecha_entra = request.POST.get("fecha_entrada")
          fecha_sali = request.POST.get("fecha_salida")
         
          importe_otros_gast= request.POST.get("importe_otros_gasto")
          
          #descuento= request.POST.get("descuento")
          descuento= request.POST.get("descuento_importe_noche")
          
        

     
          importeEstadia =calcularImporteEstadia(request, fecha_entra, fecha_sali, habitacions, importe_otros_gast)
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

          