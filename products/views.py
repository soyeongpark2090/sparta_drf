from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)


class ProductDetailAPIView(APIView):
    def put(self, request, productId):
        product = get_object_or_404(Product,pk=productId)
        serializer = ProductSerializer(product, request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response({},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,productId):
        product = get_object_or_404(Product,pk=productId)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)