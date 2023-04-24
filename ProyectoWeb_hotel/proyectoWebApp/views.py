from django.shortcuts import render

# Create your views here.

def inicio(request):

    return render(request,"proyectoWebApp/inicio.html")



def home(request):

    return render(request, "proyectoWebApp/home.html")