from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination

class ProductCreateListAPIView(CreateAPIView, ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    # permission_classes = [IsAuthenticated]
    #queryset은 ListAPIView의 attribute


    def get_serializer_context(self):
        # 뷰에서 request 컨텍스트를 시리얼라이저에 전달
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_permissions(self):
        # GET 요청에 대한 권한 설정
        if self.request.method == 'GET':
            return [AllowAny()]
        # POST 요청에 대한 권한 설정
        return [IsAuthenticated()]

# class ProductListAPIView(APIView):

#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products,many=True)
#         return Response(serializer.data)

#     @permission_classes([IsAuthenticated])
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#         return Response(serializer.data)




class ProductDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, productId):
        product = get_object_or_404(Product,pk=productId)
        if product.user == request.user:
            serializer = ProductSerializer(product, request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        return Response({"error":"권한이 없는 사용자입니다"},status=status.HTTP_403_FORBIDDEN)
    
    def delete(self,request,productId):
        product = get_object_or_404(Product,pk=productId)
        if product.user == request.user:
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error":"권한이 없는 사용자입니다"},status=status.HTTP_403_FORBIDDEN)