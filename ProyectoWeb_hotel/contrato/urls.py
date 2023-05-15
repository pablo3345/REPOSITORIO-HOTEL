
from django.urls import path
from . import views





urlpatterns = [

    path('', views.mostrarContrato, name="Contrato"), #contrato es la url que le pase al nav del padre a los botones
    #path('guardarHuesped', views.mostrarContrato, name="guardarHuesped"),
    path('modificarHuesped', views.modificarHuesped, name="modificarHuesped"),
    path('modificarTablaHuesped/<int:id_huesped>/', views.modificarTablaHuesped, name="modificarTablaHuesped"),
    path('eliminarHuesped/<int:id_huesped>/', views.eliminarHuesped, name="eliminarHuesped"),
    path('guardarContrato', views.guardarContrato, name="guardarContrato")
    
    
   

]