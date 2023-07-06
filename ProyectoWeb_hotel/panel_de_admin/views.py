from django.shortcuts import render
from habitacion.models import Habitacion
from contrato.models import Contrato
import datetime

# Create your views here.

def mostrarPanel(request):
  
  
    habitacion = Habitacion.objects.all()
    contrato = Contrato.objects.all()
    #habitacion = Habitacion()
    
    
   #------------DIAGRAMA-------------------
    contratos = Contrato.objects.all()
    ultimoFecha = datetime.datetime.now()
    ultimo= ultimoFecha.year
    

    
    enero=list()
    febrero=list()
    marzo=list()
    abril=list()
    mayo=list()
    junio=list()
    julio=list()
    agosto=list()
    septiembre=list()
    octubre=list()
    noviembre=list()
    diciembre=list()
    #------------
    cantidadEnero=0
    
    cantidadFebrero=0
    cantidadMarzo=0
    cantidadAbril=0
    cantidadMayo=0
    
    cantidadJunio=0
    cantidadJulio=0
    cantidadAgosto=0
    cantidadSeptiembre=0
    cantidadOctubre=0
    cantidadNoviembre=0
    cantidadDiciembre=0
    
    
    
    
    
   
    
    
    #  #---------------------------------------timeDelta-----------------------------------------------
    #fecha_sali = request.POST.get("fecha_salida")

     
    #fechaConvertida2 = datetime.datetime.strptime(fecha_sali, '%Y-%m-%dT%H:%M')
   
    #dia_delta = datetime.timedelta(seconds=1)
    #fechaFutura = fechaConvertida2+dia_delta
    
     #-----------------------------------------------------------------------------------------------
  
    
    
    habitacionesLibres = list()
   # habitacionesPostOcupadas = list()
    habitacionesNoLimpias = list()
    #----------------------------
    habitaciones_post = list()
    habitacionesOcupadas = list()
    #-----------traer el ultimo elemento de la lista----------
    ultimo_ocupado=list()
    ultimo_Post=list()
    
    
    
    
    
    
   
    
    
    
    for habi in habitacion:
      if habi.estado =="Null": # and habi.esta_limpia =="SI": (le saques esto al if)
          habitacionesLibres.append(habi)
          
      
          
          
    """  for habi2 in habitacion:
      if habi2.esta_limpia =="NO" and habi2.estado=="ocupada":
          habitacionesNoLimpias.append(habi2)
          """
          
    
          
        
    for contra in contrato:
       fecha_sali = contra.fecha_salida
       hoy = datetime.datetime.now()
       #fechaConvertida2 = datetime.datetime.strptime(fecha_sali, '%Y-%m-%dT%H:%M')
      # dia_delta = datetime.timedelta(seconds=1)
      # fecha_futura = fecha_sali+dia_delta
     
      
      
      
       if hoy >= fecha_sali and contra.habitacion.estado == "ocupada" and contra.estado==True: # le agregue el true
         
          habitaciones_post.append(contra)
         # ultimo_Post= habitaciones_post[-1]
        
       
       elif  fecha_sali > hoy and contra.habitacion.estado == "ocupada" and contra.estado==True:
           habitacionesOcupadas.append(contra)
          # ultimo_ocupado= habitacionesOcupadas[-1]
          
          
          #--------------------------------DIAGRAMA----------------------------------------------------
          
          
    for con in contratos:
       #---------------------------enero------------------------------------------------------------
       if con.fecha_entrada.month==1 and con.fecha_salida.month==1 and con.fecha_entrada.year==ultimo:
         enero.append(con)
         cantidadEnero= len(enero)
         #-----------------------------------------------------------------------------------------------
          #---------------------------febrero------------------------------------------------------------
       elif con.fecha_entrada.month==2 and con.fecha_salida.month==2 and con.fecha_entrada.year==ultimo:
         febrero.append(con)
         cantidadFebrero= len(febrero)
         #-----------------------------------------------------------------------------------------------
          #---------------------------marzo------------------------------------------------------------
       elif con.fecha_entrada.month==3 and con.fecha_salida.month==3 and con.fecha_entrada.year==ultimo:
         marzo.append(con)
         cantidadMarzo= len(marzo)
         #-----------------------------------------------------------------------------------------------
          #---------------------------abril------------------------------------------------------------
       elif con.fecha_entrada.month==4 and con.fecha_salida.month==4 and con.fecha_entrada.year==ultimo:
         abril.append(con)
         cantidadAbril= len(abril)
         #-----------------------------------------------------------------------------------------------
          #---------------------------mayo------------------------------------------------------------
       elif con.fecha_entrada.month==5 and con.fecha_salida.month==5 and con.fecha_entrada.year==ultimo:
         mayo.append(con)
         cantidadMayo= len(mayo)
         #-----------------------------------------------------------------------------------------------
         
       #---------------------------junio------------------------------------------------------------
       elif con.fecha_entrada.month==6 and con.fecha_salida.month==6 and con.fecha_entrada.year==ultimo:
         junio.append(con)
         cantidadJunio= len(junio)
         #-----------------------------------------------------------------------------------------------
         
           #---------------------------julio------------------------------------------------------------
       elif con.fecha_entrada.month==7 and con.fecha_salida.month==7 and con.fecha_entrada.year==ultimo:
         julio.append(con)
         cantidadJulio= len(julio)
         #-----------------------------------------------------------------------------------------------
          #---------------------------agosto------------------------------------------------------------
       elif con.fecha_entrada.month==8 and con.fecha_salida.month==8 and con.fecha_entrada.year==ultimo:
         agosto.append(con)
         cantidadAgosto= len(agosto)
         #-----------------------------------------------------------------------------------------------
          #---------------------------septiembre------------------------------------------------------------
       elif con.fecha_entrada.month==9 and con.fecha_salida.month==9 and con.fecha_entrada.year==ultimo:
         septiembre.append(con)
         cantidadSeptiembre= len(septiembre)
         #-----------------------------------------------------------------------------------------------
          #---------------------------octubre------------------------------------------------------------
       elif con.fecha_entrada.month==10 and con.fecha_salida.month==10 and con.fecha_entrada.year==ultimo:
         octubre.append(con)
         cantidadOctubre= len(octubre)
         #-----------------------------------------------------------------------------------------------
          #---------------------------noviembre------------------------------------------------------------
       elif con.fecha_entrada.month==11 and con.fecha_salida.month==11 and con.fecha_entrada.year==ultimo:
         noviembre.append(con)
         cantidadNoviembre= len(noviembre)
         #-----------------------------------------------------------------------------------------------
          #---------------------------diciembre------------------------------------------------------------
       elif con.fecha_entrada.month==12 and con.fecha_salida.month==12 and con.fecha_entrada.year==ultimo:
         diciembre.append(con)
         cantidadDiciembre= len(diciembre)
         #-----------------------------------------------------------------------------------------------
         
       data={"mesEnero": cantidadEnero, "mesFebrero":cantidadFebrero, "mesMarzo":cantidadMarzo, "mesAbril":cantidadAbril,
             "mesMayo": cantidadMayo, "mesJunio": cantidadJunio, "mesJulio": cantidadJulio, "mesAgosto": cantidadAgosto,
             "mesSeptiembre": cantidadSeptiembre, "mesOctubre": cantidadOctubre, "mesNoviembre":cantidadNoviembre,
             "mesDiciembre": cantidadDiciembre}
         
         
      
        
         
        
       
              
        
          
        
          
        
         
   
    
    return render(request, "panel_de_admin/index.html", {'habitacion': habitacionesLibres, 'contrato': contrato, 'habitacionesNoLimpias': habitacionesNoLimpias,
 'habitaciones_post':habitaciones_post, 'habitacionesOcupadas': habitacionesOcupadas, 'data':data})




# def datos_diagrama(request):
#     contratos = Contrato.objects.all()
#     #-----------------------------------------
#     enero=list()
#     febrero=list()
#     marzo=list()
    
#     abril=list()
#     mayo=list()
#     junio=list()
#     julio=list()
#     agosto=list()
#     septiembre=list()
#     octubre=list()
#     noviembre=list()
#     diciembre=list()
#     #----------------------------------
#     ultimoAnio = list()
    
    
    
#     ultimoFecha = datetime.datetime.now()
#     ultimo= ultimoFecha.year
    
#     probar = 100
  
  
    
# #     for contr in contratos:
# #          if contr.fecha_entrada.year>2022:
# #               ultimoAnio.append(contr)
# #               ultimo = ultimoAnio[-1]
         
    
#     for contrato in contratos:
#           if contrato.fecha_entrada.month==1 and contrato.fecha_entrada.year== contrato.fecha_entrada.year==ultimo:
#               enero.append(contrato)
#               cantidadEnero = enero.count
              
#           elif contrato.fecha_entrada.month==2 and contrato.fecha_entrada.year==ultimo:
#               febrero.append(contrato)
#               cantidadFebrero = febrero.count
              
#           elif contrato.fecha_entrada.month==3 and contrato.fecha_entrada.year==ultimo:
#               marzo.append(contrato)
#               cantidadMarzo = marzo.count
              
#           elif contrato.fecha_entrada.month==4 and contrato.fecha_entrada.year==ultimo:
#               abril.append(contrato)
#               cantidadAbril = abril.count
              
#           elif contrato.fecha_entrada.month==5 and contrato.fecha_entrada.year==ultimo:
#               mayo.append(contrato)
#               cantidadMayo = mayo.count
              
#           elif contrato.fecha_entrada.month==6 and contrato.fecha_entrada.year==ultimo:
#               junio.append(contrato)
#               cantidadJunio = junio.count
              
#           elif contrato.fecha_entrada.month==7 and contrato.fecha_entrada.year==ultimo:
#               julio.append(contrato)
#               cantidadJulio = julio.count
              
#           elif contrato.fecha_entrada.month==8 and contrato.fecha_entrada.year==ultimo:
#               agosto.append(contrato)
#               cantidadAgosto = agosto.count
              
#           elif contrato.fecha_entrada.month==9 and contrato.fecha_entrada.year==ultimo:
#               septiembre.append(contrato)
#               cantidadSeptiembre = septiembre.count
              
#           elif contrato.fecha_entrada.month==10 and contrato.fecha_entrada.year==ultimo:
#               octubre.append(contrato)
#               cantidadOctubre = octubre.count
              
#           elif contrato.fecha_entrada.month==11 and contrato.fecha_entrada.year==ultimo:
#               noviembre.append(contrato)
#               cantidadNoviembre = noviembre.count
              
#           elif contrato.fecha_entrada.month==12 and contrato.fecha_entrada.year==ultimo:
#               diciembre.append(contrato)
#               cantidadDiciembre = diciembre.count
              
              
#     data={'enero': cantidadEnero, 'febrero': cantidadFebrero, 'marzo': cantidadMarzo, 'abril': cantidadAbril,
#                'mayo': cantidadMayo, 'junio': cantidadJunio, 'julio': cantidadJulio, 'agosto': cantidadAgosto,
#                'septiembre': cantidadSeptiembre, 'octubre': cantidadOctubre, 'noviembre': cantidadNoviembre, 'diciembre': cantidadDiciembre}
              
              
              
         
         
#     return render(request, "panel_de_admin/diagramas.html", {'data': data, 'ultimo': ultimo, 'probar':probar})
              
              
     
    
    
    
    