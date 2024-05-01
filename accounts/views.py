from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer, UserProfileSerializer, UserInfoChangeSerializer
from .models import NewUser
from rest_framework.request import Request
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenBlacklistView, TokenObtainPairView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework.exceptions import ValidationError
from rest_framework.exceptions import PermissionDenied

class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            newuser = serializer.save()
            if newuser:
                return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        try:
            # user_profile = NewUser.objects.get(user_name=username)
            user_profile = get_object_or_404(NewUser,user_name = username)
            serializer = UserProfileSerializer(user_profile)
            return Response(serializer.data)
        except NewUser.DoesNotExist:
            return Response({"error": "일치하는 유저 프로필이 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        

    def put(self, request, username):
        if request.user.user_name == username:
            user = get_object_or_404(NewUser, user_name = username)
            serializer = UserInfoChangeSerializer(user, request.data, partial=True)

            if serializer.is_valid(raise_exception=True):
                email = serializer.validated_data.get("email")
                if email and NewUser.objects.exclude(pk=request.user.user_name).filter(email=email).exists():
                    return Response({"error":"이미 사용 중인 이메일 입니다"})

                serializer.save()
                return Response(serializer.data)
        return Response({"error":"권한이 없는 사용자입니다"})





class LogoutAPIView(TokenBlacklistView):
    # permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs) 
        return Response({"message":"로그아웃 되었습니다"})