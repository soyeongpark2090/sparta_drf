from django.urls import path
from .views import CustomUserCreate
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)


app_name = 'accounts'

urlpatterns = [
    path('', CustomUserCreate.as_view(), name="create_user"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/',views.LogoutAPIView.as_view()),
    path('<str:username>/',views.ProfileView.as_view()),

] 
