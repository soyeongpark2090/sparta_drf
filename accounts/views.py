from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer, UserProfileSerializer
from .models import NewUser
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        try:
            # username에 해당하는 사용자 프로필 조회
            user_profile = NewUser.objects.get(user_name=username)
            # 시리얼라이저를 사용하여 프로필 데이터 직렬화
            serializer = UserProfileSerializer(user_profile)
            return Response(serializer.data)
        except NewUser.DoesNotExist:
            return Response({"error": "User profile does not exist"}, status=status.HTTP_404_NOT_FOUND)
