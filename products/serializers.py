from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ("user",)

    def create(self, validated_data):
        # 현재 인증된 사용자를 가져옴
        user = self.context['request'].user
        # validated_data에 user 필드 추가
        validated_data['user'] = user
        # 새로운 Product 인스턴스 생성
        product = Product.objects.create(**validated_data)
        return product