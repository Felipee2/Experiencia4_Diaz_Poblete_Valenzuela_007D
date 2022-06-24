from django.urls import path
from .views import rastreos,index, carrito, comprar, login, reestablecer, registro, sobrenosotros, ubicanos,mod_perfil,eliminar_perfil
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('', index,name="index"),
    path('carrito', carrito, name="carrito"),
    path('comprar', comprar, name="comprar"),
    path('login', LoginView.as_view(template_name='login.html'), name="login"),
    path('reestablecer', reestablecer, name="reestablecer"),
    path('registro', registro, name = "registro"),
    path('mod_perfil/<id>/<password>', mod_perfil, name = "modperfil"),
    path('eliminar_perfil/<id>', eliminar_perfil, name = "eliminarperfil"),
    path('sobrenosotros', sobrenosotros, name="sobrenosotros"),
    path('ubicanos', ubicanos, name="ubicanos"),
    path('rastreo',rastreos,name="rastreo"),
]  