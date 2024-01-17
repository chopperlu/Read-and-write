from dj_rest_auth.views import LogoutView
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, permissions
from . import serializers


class UserRegisterView(generics.CreateAPIView):
    serializer_class = serializers.RegisterSerializer



class CustomLogoutView(LogoutView):
    permission_classes = (permissions.IsAuthenticated,)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserListSerializer
    # permission_classes = (permissions.IsAuthenticated,)  #листинг пока уберем чтобы посмотреть книги можно без рег. а вот почитать нужно нужно



class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    # permission_classes = (permissions.IsAuthenticated,)  #здесь также как в листинг