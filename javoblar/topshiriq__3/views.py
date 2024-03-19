from django.shortcuts import render
from rest_framework import generics
from javoblar.topshiriq__3.models import Product
from javoblar.topshiriq__3.serializers import ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

