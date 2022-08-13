from django.urls import path
from .api import *
urlpatterns = [
    path("CreateProduct",ProductListApi.as_view(),name="CreateProduct"),
    path("CreateUpdateDestroyProduct",ProductViewSet.as_view(),name="RetrieveUpdateDestroyProduct"),
    path("ListImage",ImageListApi.as_view(),name="CreateImage"),
    path("CreateUpdateDestroyImage",ImageViewSet.as_view(),name="RetrieveUpdateDestroyImage"),
]