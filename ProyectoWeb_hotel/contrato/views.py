from django.shortcuts import render
from contrato.formsContrtato import FormContrato 
from contrato.formsHuesped import FormHuesped

# Create your views here.


def guardarHuesped(request):
     form = FormHuesped()
     form2 = FormContrato()
  
    
     return render(request, "contrato/contrato.html", {'formHuesped': form, 'formContrato': form2})
 
 
 
def guardarContrato(request):
     
    form2 = FormContrato()
     
     
     
    return render(request, "contrato/contrato.html", {'formContrato': form2})




    
    
    
    







