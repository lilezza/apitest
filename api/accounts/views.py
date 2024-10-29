from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from .models import User
from .serializer import UserSerializer

class UserPostListCreate(generics.ListCreateAPIView , CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self , request , *args , **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        redirect_url = reverse('userpostlistcreate', request=request)
        return Response({'redirect': redirect_url}, status=status.HTTP_201_CREATED)


class UserPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # برگرداندن لینک در پاسخ به جای ریدایرکت
        redirect_url = reverse('userpostlistcreate', request=request)
        return Response({'redirect_url': redirect_url}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        redirect_url = reverse('userpostlistcreate' , request = request )
        return Response({'redirect': redirect_url} , status = status.HTTP_204_NO_CONTENT)


class UserPostList(APIView):
    def get(self , request , format = None):
        first_name = request.query_params.get("first_name" , "")
        if first_name:
            user_posts = User.objects.filter(first_name__icontains=first_name)
        else:
            user_posts = User.objects.all()
        serializer = UserSerializer(user_posts , many = True)
        return Response(serializer.data , status=status.HTTP_200_OK)
