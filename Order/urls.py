from django.urls import path
from .api import *
urlpatterns = [
    path("CreateOrder", ListCreateOrderAPIView.as_view(), name="CreateOrder"),
    path("RetrieveUpdateDestroyOrder", RetrieveUpdateDestroyOrderAPIView.as_view(), name="RetrieveUpdateDestroyOrder"),
    path("CreateOrderUnit", ListCreateOrderUnitAPIView.as_view(), name="CreateOrderUnit"),
    path("RetrieveUpdateDestroyOrderuit", RetrieveUpdateDestroyOrderUnitAPIView.as_view(), name="RetrieveUpdateDestroyOrderUnit"),
    path("CreateCart", ListCreateCartAPIView.as_view(), name="CreateCart"),
    path("RetrieveUpdateDestroyCart", RetrieveUpdateDestroyCartAPIView.as_view(), name="RetrieveUpdateDestroyCart")
]