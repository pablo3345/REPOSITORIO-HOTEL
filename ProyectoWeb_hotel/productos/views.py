from django.shortcuts import render
from productos.formsProducto import ProveedoresForm, InsumosForm, ProductoPublicoForm
from django.contrib import messages
from productos.models import Proveedores

# Create your views here.

def guardarProveedor(request):
    
    formProvee = ProveedoresForm()
    formInsu = InsumosForm()
    formProdPubli = ProductoPublicoForm()
    
    if request.method=="POST":
        formProvee = ProveedoresForm(request.POST)
        
        if formProvee.is_valid():
            
            formProvee.save()
            messages.success(request, "El proveedor se guardo correctamente...")
            
        else:
            messages.error(request, "El proveedor no se guardo...")
            
            
    else:
        formProvee= ProveedoresForm()
            
    
    
    
    
    
    
    
    return render(request, "productos/productos.html", {'formProveedor': formProvee, 'formInsumos': formInsu, 'formProductoPublico':formProdPubli})




def modificar_Proveedor(request):
    
    proveedores = Proveedores.objects.all()
    
    #proveedor = Proveedores.objects.get(id = id_proveedor)
    
    
    
    return render(request, "productos/modificarProveedor.html", {'proveedores': proveedores})
    
    