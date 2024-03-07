from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from app.models import *
from django.http import HttpResponse
from .forms import *
from .vistas.autor_views import *
from .vistas.usuario_views import *
