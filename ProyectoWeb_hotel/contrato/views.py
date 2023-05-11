from django.shortcuts import render
from contrato.formsContrtato import FormContrato 
from contrato.formsHuesped import FormHuesped
from django.contrib import messages


# Create your views here.


def mostrarContrato(request):
     form = FormHuesped()
     form2 = FormContrato()
  
    
     return render(request, "contrato/contrato.html", {'formHuesped': form, 'formContrato': form2})
 
 
 
def guardarHuesped(request):
     
    #form2 = FormContrato()
    #form = FormHuesped()
    
    if request.method =='POST':
         
         formHuesped =FormHuesped(request.POST)
         
         if formHuesped.is_valid():
              
              formHuesped.save()
              messages.success(request, "El huesped se guardo correctamente...")
              
         else:
              messages.error(request, "El huesped no se guardo...")
              
              
    else:
         form = FormHuesped()
         
     
     
    return render(request, "contrato/contrato.html", {'formHuesped': form})




    
    
    
    







