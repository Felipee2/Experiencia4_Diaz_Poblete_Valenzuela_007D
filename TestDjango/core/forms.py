from django import forms
from django.forms import ModelForm
from .models import UsuarioTienda


class FormUsuario(ModelForm):

    idRut= forms.CharField(min_length=9, max_length=9)
    nombre = forms.CharField(min_length=2)
    contraseña = forms.CharField(min_length=4)
    telefono = forms.CharField(min_length=9, max_length=9)

    class Meta:
        model = UsuarioTienda
        fields = ['idRut', 'nombre', 'correo', 'contraseña', 'telefono']

