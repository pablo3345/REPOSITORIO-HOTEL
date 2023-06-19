from django.urls import path
from . import views

urlpatterns = [

    path('', views.guardarProveedor, name="guardarProveedor"),
    path('modificarProveedor', views.modificar_Proveedor, name="modificarProveedor"),
    path('modificarTabla_proveedor/<int:id_proveedor>/', views.modificarTabla_proveedor, name="modificarTabla_proveedor"),
    path('eliminarProveedor/<int:id_proveedor>/', views.eliminarProveedor, name="eliminarProveedor"),
    path('guardarInsumos', views.guardarInsumos, name="guardarInsumos"),
    path('modificarInsumos', views.modificarInsumos, name="modificarInsumo"),
    path('modificarTabla_insumos/<int:id_insumos>/', views.modificar_tabla_insumos, name="modificarTabla_insumos"),
    path('eliminarInsumo/<int:id_insumo>/', views.eliminarInsumo, name="eliminarInsumo"),
    path('guardarProducto', views.guardarProducto, name="guardarProducto"),
    path('modificarProducto', views.modificarProducto, name="modificarProducto"),
    path('modificarTabla_productos/<int:id_producto>/', views.modificar_tabla_productos, name="modificarTabla_productos"),
     path('eliminarProducto/<int:id_producto>/', views.eliminarProducto, name="eliminarProducto"),
    
    
    
    
]