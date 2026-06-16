from rest_framework import serializers
from .models import *

#login api
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = '__all__ '


    def create(self, validated_data):

        user = User.objects.create_user(
            **validated_data
        )

        return user
    
    '''
    from rest_framework import serializers
    from .models import User


    class RegisterSerializer(serializers.ModelSerializer):

        password2 = serializers.CharField(
            write_only=True
        )


        class Meta:

            model = User

            fields = [
                "email",
                "username",
                "password",
                "password2"
            ]


            extra_kwargs = {

                "password": {
                    "write_only": True
                }

            }

        def validate(self,data,value):

            if data["password"] != data["password2"]:
                raise serializers.ValidationError(
                    "Passwords do not match"
                )

            return data

            if User.objects.filter(email=value).exists():

            raise serializers.ValidationError(
                "Email already exists"
                )

            return value


        def create(self, validated_data):

            validated_data.pop(
                "password2"
            )


            user = User.objects.create_user(
                **validated_data
            )


            return user
    '''

class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()

    password = serializers.CharField(
        write_only=True
    )


    def validate(self, data):

        email = data.get("email")

        password = data.get("password")


        user = authenticate(
            email=email,
            password=password
        )


        if user is None:

            raise serializers.ValidationError(
                "Invalid email or password"
            )


        refresh = RefreshToken.for_user(user)


        return {

            "refresh": str(refresh),

            "access": str(
                refresh.access_token
            )

        }