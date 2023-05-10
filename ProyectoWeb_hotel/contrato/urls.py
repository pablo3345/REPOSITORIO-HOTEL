
from django.urls import path
from . import views





urlpatterns = [

    path('', views.guardarHuesped, name="Contrato"), #contrato es la url que le pase al nav del padre a los botones
   # path('guardarHuesped', views.guardarHuesped, name="guardarHuesped")
    
   

]