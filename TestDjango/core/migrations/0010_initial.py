# Generated by Django 4.0.5 on 2022-06-20 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0009_delete_productos_delete_usuariotienda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('idProd', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('stock', models.IntegerField(verbose_name='Stock')),
                ('image', models.ImageField(upload_to='core/static/imgProd')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioTienda',
            fields=[
                ('idRut', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Rut')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('correo', models.CharField(max_length=50, verbose_name='Correo')),
                ('contraseña', models.CharField(max_length=20, verbose_name='Contraseña')),
                ('telefono', models.CharField(max_length=9, verbose_name='Telefono')),
            ],
        ),
    ]
