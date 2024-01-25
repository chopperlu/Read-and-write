

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.db import models
from rest_framework import serializers

from comment.serializers import CommentSerializer


class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True, required=True)
    password2 = serializers.CharField(min_length=8, write_only=True, required=True)
    email = serializers.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'password2', 'email')
    def validate(self, attrs):
        password2 = attrs.pop('password2')
        if password2 != attrs['password']:
            raise serializers.ValidationError('Passwords must match!')
        validate_password(attrs['password'])
        return attrs
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')



class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


