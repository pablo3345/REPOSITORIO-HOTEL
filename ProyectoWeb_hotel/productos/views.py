from django.shortcuts import render
from productos.formsProducto import ProveedoresForm, InsumosForm, ProductoPublicoForm

# Create your views here.

def guardarProveedor(request):
    
    formProveedor = ProveedoresForm()
    formInsumos = InsumosForm()
    formProductoPublico = ProductoPublicoForm()
    
    
    
    
    
    
    
    return render(request, "productos/productos.html", {'formProveedor': formProveedor, 'formInsumos': formInsumos, 'formProductoPublico':formProductoPublico})
