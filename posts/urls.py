
from django.contrib import admin
from django.urls import path
from app.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [path('admin/', admin.site.urls)]

url_autor = [ 
    path('crear_articulo/',crear_articulo),
    path('editar_articulo/<int:id>',editar_articulo),
    path('agregar_imagen/<int:id>',agregar_imagen),
    path('agregar_texto/<int:id>',agregar_texto)
    ]

url_usuario = [ 
    path('home/',home),
    path('',home),
    path('articulo/<int:id>', articulo)
    ]

urlpatterns += url_autor
urlpatterns += url_usuario




urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)