from django.shortcuts import render
from productos.formsProducto import ProveedoresForm

# Create your views here.

def guardarProveedor(request):
    
    formProveedor = ProveedoresForm()
    
    
    
    
    
    
    return render(request, "productos/productos.html", {'formProveedor': formProveedor})
