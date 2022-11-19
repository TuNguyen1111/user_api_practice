from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer
from .permissions import CanViewListProducts, CanEditProducts

# Create your views here.

@api_view(['GET'])
@permission_classes([CanViewListProducts])
def list_api(requets):
    products = Product.get_products()
    serializer = ProductSerializer(products, many=True).data
    return Response(serializer)


@api_view(['POST'])
@permission_classes([CanEditProducts])
def create_product(request):
    data = request.data
    serialzer = ProductSerializer(data=data)
    if serialzer.is_valid():
        serialzer.save()
    return Response(serialzer.data)


@api_view(['POST'])
def update_product(request, pk):
    task = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
