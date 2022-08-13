from rest_framework import generics
from .serializers import *
## list_create Order api
class  ListCreateOrderAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class =  OrderSerializer()

# retrieve_update_destroy Order api
class RetrieveUpdateDestroyOrderAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class =  OrderSerializer()
    lookup_field = 'id'
    
## list_create Order api
class  ListCreateOrderUnitAPIView(generics.ListCreateAPIView):
    queryset = OrderUnit.objects.all()
    serializer_class =  OrderUnitSerializer()

# retrieve_update_destroy Order api
class RetrieveUpdateDestroyOrderUnitAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderUnit.objects.all()
    serializer_class =  OrderUnitSerializer()
    lookup_field = 'id'
## list_create Order api
class  ListCreateCartAPIView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class =  CartSerializer()

# retrieve_update_destroy Order api
class RetrieveUpdateDestroyCartAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class =  CartSerializer()
    lookup_field = 'id'