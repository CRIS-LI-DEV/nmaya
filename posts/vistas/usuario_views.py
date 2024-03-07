from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from app.models import *
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
def home(request):
    todos_los_articulos = Articulo.objects.all()
    context = {'articulos':todos_los_articulos,'numero':250}
    print(settings.STATIC_URL) 
    print(settings.STATIC_ROOT) 
    print(settings.BASE_DIR)
    print(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)) 
    return render(request, 'interfaz_usuario/home.html', context)  
     


def articulo(request,id):
    articulo_buscado  = Articulo.objects.get(id = id)
    textos_buscados  = Texto.objects.filter(articulo_id= id)
    imagenes_buscadas  = Imagen.objects.filter(articulo_id= id)
    
    context={
        'articulo':articulo_buscado,
        'textos':textos_buscados,
        'imagenes':imagenes_buscadas 
        }
    return render(request,'interfaz_usuario/articulo.html',context)