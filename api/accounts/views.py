from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User
from .serializer import UserSerializer

class UserPostListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self , request , *args , **kwargs):
        User.objects.all().delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class UserPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"

class UserPostList(APIView):
    def get(self , request , format = None):
        first_name = request.query_params.get("first_name" , "")
        if first_name:
            user_posts = User.objects.filter(first_name__icontains=first_name)
        else:
            user_posts = User.objects.all()
        serializer = UserSerializer(user_posts , many = True)
        return Response(serializer.data , status=status.HTTP_200_OK)
