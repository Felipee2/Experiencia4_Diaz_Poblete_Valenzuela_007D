from django.urls import path
from rest_tienda.views import lista_productos,detalle_productos

urlpatterns = [
    path('lista_productos',lista_productos,name="lista_productos"),
    path('detalle_productos/<id>',detalle_productos, name="detalle_productos"),
]