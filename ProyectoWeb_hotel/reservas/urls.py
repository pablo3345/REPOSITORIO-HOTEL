from django.urls import path
from . import views

urlpatterns = [

    path('', views.mostrar_reserva, name="mostrar_reservas"),
    path('guardarReserva', views.guardarReserva, name="guardarReserva"),
    path('modificarReserva', views.modificarReservas, name="ModificarReservas"),
    path('enviarContrato/<int:id_reserva>/', views.enviar_a_contrato, name="enviarContrato")
    # path('guardarHuesped', views.guardarHuesped, name="guardarHuesped"),
   
    
]