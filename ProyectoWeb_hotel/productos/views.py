from django.shortcuts import render, redirect
from productos.formsProducto import ProveedoresForm, InsumosForm, ProductoPublicoForm
from django.contrib import messages
from productos.models import Proveedores, Insumos

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
        return redirect('guardarProveedor')
            
            
    else:
        formProvee= ProveedoresForm()
            
    
    
    
    
    
    
    
    return render(request, "productos/productos.html", {'formProveedor': formProvee, 'formInsumos': formInsu, 'formProductoPublico':formProdPubli})




def modificar_Proveedor(request):
    
    proveedores = Proveedores.objects.all()
    
    #proveedor = Proveedores.objects.get(id = id_proveedor)
    
    
    
    return render(request, "productos/modificarProveedor.html", {'proveedores': proveedores})
    
    
    
def modificarTabla_proveedor(request, id_proveedor):
    
    formProveedor= ProveedoresForm()
    
    proveedor = Proveedores.objects.get(id = id_proveedor)
    
    if request.method == "POST":
        
       nombre_proveedor = request.POST.get("nombre_proveedor")
       apellido =request.POST.get("apellido")
       direccion = request.POST.get("direccion")
       telefono= request.POST.get("telefono")
       mail= request.POST.get("mail")
       nombre_empresa= request.POST.get("nombre_empresa")
       algun_otro_dato =  request.POST.get("algun_otro_dato")
       
       proveedor.nombre_proveedor= nombre_proveedor
       proveedor.apellido=apellido
       proveedor.direccion=direccion
       proveedor.telefono=telefono
       proveedor.mail=mail
       proveedor.nombre_empresa=nombre_empresa
       proveedor.algun_otro_dato=algun_otro_dato
       
       try:
           proveedor.save()
           messages.success(request, "El proveedor se actualizo correctamente...")
           return redirect('modificarProveedor')
            
       except:
            messages.error(request, "El proveedor no se actualizo...")
            return redirect('modificarProveedor')
    
    
    
    else:
        formProveedor = ProveedoresForm(instance=proveedor)
        
        
    return render(request, "productos/modificarTabla_proveedor.html", {'formProveedor': formProveedor})
   
   
def eliminarProveedor(request, id_proveedor):
    proveedor = Proveedores.objects.get(id = id_proveedor)
    
    try:
        proveedor.delete()
        messages.success(request, "El proveedor se elimino correctamente...")
        return redirect('modificarProveedor')
    
    except:
        messages.error(request, "El proveedor no se elimino...")
        return redirect('modificarProveedor')
    
    
    
    
def guardarInsumos(request):
    formProvee = ProveedoresForm()
    formInsu = InsumosForm()
    formProdPubli = ProductoPublicoForm()
    
    if request.method=="POST":
        formInsu = InsumosForm(request.POST)
        
        if formInsu.is_valid():
            
            formInsu.save()
            messages.success(request, "El insumo se guardo correctamente...")
            
            
        else:
            messages.error(request, "El insumo no se guardo...")
        return redirect('guardarInsumos')
            
            
    else:
        formInsu= InsumosForm()
            
    
    
    
    
    
    
    
    return render(request, "productos/productos.html", {'formProveedor': formProvee, 'formInsumos': formInsu, 'formProductoPublico':formProdPubli})



def modificarInsumos(request):
    
    insumos= Insumos.objects.all()
    
    
    
    return render(request, "productos/modificarInsumos.html", {'insumos': insumos})



def modificar_tabla_insumos(request, id_insumos):
    
    insumo = Insumos.objects.get(id = id_insumos)
    formInsumos = InsumosForm()
    
    
    
    
    
    
    if request.method=="POST":
        
        nombre_insumos = request.POST.get("nombre_insumos")
        marca_insumos =  request.POST.get("marca_insumos")
        precio =  request.POST.get("precio")
        medida =  request.POST.get("medida")
       
        algun_otro_dato=  request.POST.get("algun_otro_dato")
        disponibilidad =  request.POST.get("disponibilidad")
        #---------------------------------------------------
        id = request.POST.get("proveedor")
   
        proveedor_id= Proveedores.objects.get(id=id)
        #-----------------------------------------
        
        
        insumo.nombre_insumos=nombre_insumos
        insumo.marca_insumos= marca_insumos
        insumo.precio= precio
        insumo.medida= medida
        insumo.proveedor= proveedor_id
        insumo.algun_otro_dato= algun_otro_dato
        insumo.disponibilidad= disponibilidad
        
        try:
            insumo.save()
            messages.success(request, "El insumo se actualizo correctamente...")
            
        except:
             messages.error(request, "El insumo no se actualizo...")
             
        return redirect('modificarInsumo')
    
    
    
    else:
        formInsumos = InsumosForm(instance=insumo)
        
        
    return render(request, "productos/modificarTabla_Insumos.html", {'formInsumos': formInsumos})



def eliminarInsumo(request, id_insumo):
    insumo= Insumos.objects.get(id= id_insumo)
    
    
    try:
        insumo.delete()
        messages.success(request, "El insumo se elimino correctamente...")
        
    except:
         messages.error(request, "El insumo no se elimino...")
         
    return redirect('modificarInsumo')

        
            
        
      