from django.urls import path
from .views import CustomUserCreate

app_name = 'accounts'

urlpatterns = [
    path('', CustomUserCreate.as_view(), name="create_user"),
]
