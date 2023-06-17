from django.urls import path
from . import views

urlpatterns = [

    path('', views.guardarProveedor, name="guardarProveedor"),
    path('modificarProveedor', views.modificar_Proveedor, name="modificarProveedor"),
]