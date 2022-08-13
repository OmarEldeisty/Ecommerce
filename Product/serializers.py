from rest_framework import serializers
from .models import (Product, Image)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Product
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Image

