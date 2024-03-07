from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from app.models import *
from django.http import HttpResponse
from app.forms import *

def crear_articulo(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        bajada = request.POST['bajada']
        nuevo_articulo = Articulo()
        nuevo_articulo.titulo = titulo
        nuevo_articulo.bajada = bajada
     
        nuevo_articulo.save()


        return redirect (f'/editar_articulo/{nuevo_articulo.id}')
    else:
        formulario = ArticuloForm()
        return render(request,'interfaz_autor/crear_articulo.html',{ 'formulario':formulario   })
    

def editar_articulo(request,id):
    articulo_buscado = Articulo.objects.get(id = id)
    lista_de_parrafos = Texto.objects.filter(articulo_id = id)
    lista_de_Imagenes = Imagen.objects.filter(articulo_id = id)

    context = {'articulo':articulo_buscado,'parrafos':lista_de_parrafos, 'imagenes':lista_de_Imagenes}
    return render(request, 'interfaz_autor/editar_articulo.html',context)


def agregar_texto(request,id):

    if request.method == 'POST':
        texto_nuevo  = request.POST['texto'] 
        lugar_del_parrafo = request.POST['lugar'] 
        
        texto_creado = Texto()
        
        texto_creado.texto  = texto_nuevo
        
        texto_creado.lugar = lugar_del_parrafo
        articulo_buscado = Articulo.objects.get(id = id)
        texto_creado.articulo= articulo_buscado
        
        
        texto_creado.save()
        return redirect (f'editar_articulo/{articulo_buscado.id}')

    else:
        formulario_texto =TextoForm() 
        context = { 'form': formulario_texto }
        print(formulario_texto)
        return render(request,'interfaz_autor/agregar_texto.html', context)
    



def agregar_imagen(request,id):
    print('ENTRE A AGREGAR IMAGEN')
    if request.method == 'POST':
        articulo_buscado = Articulo.objects.get(id = id)
        imagen_nueva = Imagen()
        archivo = request.FILES['archivo']
        lugar = request.POST['lugar']
        imagen_nueva.archivo = archivo
        imagen_nueva.lugar = lugar
        imagen_nueva.articulo = articulo_buscado
        imagen_nueva.save()

        return redirect (f'/editar_articulo/{articulo_buscado.id}')
    else:
        form = ImagenForm()
        return render(request, 'interfaz_autor/agregar_imagen.html', {'form': form})

    
