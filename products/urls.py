from django.urls import path
from . import views


urlpatterns = [
    path("", views.ProductCreateListAPIView.as_view()),
    path("<int:productId>", views.ProductDetailAPIView.as_view()),
]