from django.db import models


# Create your models here.
class UsuarioTienda(models.Model):
    idRut = models.CharField(primary_key=True, max_length=10, verbose_name = 'Rut')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    correo = models.CharField(max_length=50, verbose_name='Correo')
    contraseña = models.CharField(max_length=20, verbose_name='Contraseña') 
    telefono = models.CharField(max_length=9, verbose_name='Telefono')
    
    def __str__(self):
         return self.idRut

class Productos(models.Model):
    idProd = models.IntegerField(primary_key=True,verbose_name='Id')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    precio = models.IntegerField(verbose_name='Precio')
    stock  = models.IntegerField(verbose_name='Stock')
    image = models.ImageField(upload_to='static/imgProd')