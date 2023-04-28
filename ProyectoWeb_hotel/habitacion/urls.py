
from django.urls import path
from . import views





urlpatterns = [

    path('', views.mostrarHabitacion, name="Habitacion"),
    path('modificarHabitacion', views.actualizarHabitacion, name="modificarHabitacion"),
    path('actualizarTabla/<int:id_habitacion>/', views.tabla_modificar, name="actualizarTabla"),
    path('eliminar/<int:id_habitacion>/', views.eliminarHabitacion, name="eliminar")

]
