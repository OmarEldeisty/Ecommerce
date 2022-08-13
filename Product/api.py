from .serializers import (ImageSerializer, ProductSerializer)
from rest_framework import generics
from .models import Image, Product
class ProductListApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'

class ImageListApi(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    lookup_field = 'id'