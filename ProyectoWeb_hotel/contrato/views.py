from django.shortcuts import render

# Create your views here.


def mostrarContrato(request):
    
    return render(request, "contrato/contrato.html")
