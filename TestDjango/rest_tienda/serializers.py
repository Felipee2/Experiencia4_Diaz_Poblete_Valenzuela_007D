from rest_framework import serializers
from core.models import Productos

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Productos
        fields = '__all__'