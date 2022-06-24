from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Productos
from .serializers import ProductoSerializer

@csrf_exempt
@api_view(['GET','POST'])
def lista_productos(request):
    if request.method == 'GET':
        productos = Productos.objects.all()
        serializer = ProductoSerializer(productos,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        serializer = VehiculoSerializer(data= data.request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def detalle_productos (request, id):
    try:
        productos = Productos.objects.get(idProd=id)
    except Productos.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductoSerializer(productos)
        return Response(serializer.data)
    if request.method == 'PUT':
        #data = JSONParser().parse(request)
        serializer = ProductoSerializer(productos, data= data.request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error, status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        productos.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)