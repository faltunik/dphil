from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *
from .serializer import *
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['id'] = user.id
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,) # why we are doing this?

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data) 
        try:
            if serializer.is_valid():             
                serializer.save() 
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("Error is :"  ,e)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






        






