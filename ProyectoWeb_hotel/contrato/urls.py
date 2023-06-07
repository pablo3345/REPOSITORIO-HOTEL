
from django.urls import path
from . import views





urlpatterns = [

    path('', views.mostrarContrato, name="Contrato"), #contrato es la url que le pase al nav del padre a los botones
    #path('guardarHuesped', views.mostrarContrato, name="guardarHuesped"),
    path('modificarHuesped', views.modificarHuesped, name="modificarHuesped"),
    path('modificarTablaHuesped/<int:id_huesped>/', views.modificarTablaHuesped, name="modificarTablaHuesped"),
    path('eliminarHuesped/<int:id_huesped>/', views.eliminarHuesped, name="eliminarHuesped"),
    path('guardarContrato', views.guardarContrato, name="guardarContrato"),
    path('modificarContrato', views.modificarContrato, name="modificarContrato"),
    path('modificarTablaContrato/<int:id_contrato>/', views.modificarTablaContrato, name="modificarTablaContrato"),
    path('eliminarContrato/<int:id_contrato>/', views.eliminarContrato, name="eliminarContrato"),
    path('calcularTotal', views.calcularTotal, name="calcularTotal"),
    path('habilitar_ocupadas/<int:id_habitacion>/', views.habilitar_ocupadas, name="habilitar_ocupadas") # para hablitar las habitaciones ocupadas
  
    
    
    
   

]