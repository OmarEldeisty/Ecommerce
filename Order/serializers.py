from rest_framework import serializers
from .models import (Order, Cart, OrderUnit)

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Order

class OrderUnitSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = OrderUnit

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Cart
