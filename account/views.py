from dj_rest_auth.views import LogoutView
from django.contrib.auth.models import User
from rest_framework import generics, permissions

from like.serializers import MylibrarySerializer
from . import serializers



class UserMylibrariesView(generics.ListAPIView):
    serializer_class = MylibrarySerializer
    permission_classes = [permissions.IsAuthenticated,]

    def get_queryset(self):
        user = self.request.user
        return user.mylibraries.all()

class UserRegisterView(generics.CreateAPIView):
    serializer_class = serializers.RegisterSerializer

class CustomLogoutView(LogoutView):
    permission_classes = (permissions.IsAuthenticated,)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserListSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer






