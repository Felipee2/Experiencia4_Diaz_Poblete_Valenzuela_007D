from django.shortcuts import render, redirect
from .models import UsuarioTienda,Productos
from .forms import FormUsuario
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import auth
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def carrito(request):
    return render(request, 'core/carrito.html')

def comprar(request):
    return render(request, 'core/comprar.html')

def rastreos (request):
    return render(request, 'core/rastreoPedido.html')





def reestablecer(request):
    return render(request, 'core/reestablecer.html')



def mostrarproductos(request):
    productos= Productos.objects.all()
    datos= {
        'productos': productos
    }
    return render(request, 'core/perfil.html',datos)



def registro(request):
    datos={
        'form':FormUsuario()
    }
    if request.method == 'POST':
        formulario= FormUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Registrado correctamente"
    return render(request, 'core/registro.html',datos)

def mod_perfil(request, id,password):
    try:
        usuarios = UsuarioTienda.objects.get(idRut=id,contraseña=password)
        datos = {
            'form': FormUsuario(instance=usuarios)
        }
        if request.method == 'POST':
            formulario = FormUsuario(data=request.POST, instance=usuarios)
            if formulario.is_valid():
                formulario.save()
                datos['mensaje'] = "Modificado correctamente"
        return render(request, 'core/mod_perfil.html', datos)
    except ObjectDoesNotExist:
        return render(request, 'core/mod_perfil.html', datos)

    
    


def login(request):

    return render(request, 'core/login.html')




def eliminar_perfil(request, id):
    usuarios = UsuarioTienda.objects.get(idRut=id)
    usuarios.delete()
    return redirect(to="perfil")

def sobrenosotros(request):
    return render(request, 'core/sobrenosotros.html')

def ubicanos(request):
    return render(request, 'core/ubicanos.html')


