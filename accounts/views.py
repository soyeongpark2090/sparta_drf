from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer, UserProfileSerializer
from .models import NewUser
from rest_framework.request import Request
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenBlacklistView, TokenObtainPairView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

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
            user_profile = NewUser.objects.get(user_name=username)
            serializer = UserProfileSerializer(user_profile)
            return Response(serializer.data)
        except NewUser.DoesNotExist:
            return Response({"error": "일치하는 유저 프로필이 없습니다."}, status=status.HTTP_404_NOT_FOUND)


class LogoutAPIView(TokenBlacklistView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, *args, **kwargs):
        try:
            refresh_token = request.data.get('refresh')
            if not refresh_token:
                return Response({'error': 'refresh 토큰이 필요합니다.'}, status=status.HTTP_400_BAD_REQUEST)

            # 블랙리스트에 refresh 토큰 추가하여 로그아웃
            RefreshToken(refresh_token).blacklist()

            return Response({'message': '로그아웃 되었습니다.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)