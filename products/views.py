from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

class ProductListAPIView(APIView):
    def post(self, request):
        pass