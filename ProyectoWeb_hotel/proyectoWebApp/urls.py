from proyectoWebApp import views
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [

    path('', views.inicio, name="Inicio"),
    path('home', views.home, name="Home"),

]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #para las imagenes (media)
