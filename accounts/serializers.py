from rest_framework import serializers
from accounts.models import NewUser

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'password','nickname','name','birth','gender','bio')
        extra_kwargs = {
            'password': {'write_only': True},
            }


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['user_name', 'email','nickname','name','birth','gender','bio']


class UserInfoChangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewUser
        fields = ['email', 'name','nickname','birth','gender','bio']

    # def validate_email(self, value):
    #     if NewUser.objects.exclude(pk=self.instance.pk).filter(email=value).exists():
    #         raise serializers.ValidationError("이미 사용 중인 이메일입니다.")
    #     return value
    # #이미 모델에서 email field에 설정한 unique=True의 기본메시지가 뜸