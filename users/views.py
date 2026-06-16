from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from .serializers import *

#for login api
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response



class RegisterView(CreateAPIView):

    serializer_class = RegisterSerializer

class LoginView(GenericAPIView):

    serializer_class = LoginSerializer


    def post(self, request):

        serializer = self.get_serializer(
            data=request.data
        )


        serializer.is_valid(
            raise_exception=True
        )


        return Response(
            serializer.validated_data
        )