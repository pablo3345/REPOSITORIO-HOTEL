
from django.urls import path
from . import views





urlpatterns = [

    path('', views.mostrarContrato, name="Contrato")
   

]