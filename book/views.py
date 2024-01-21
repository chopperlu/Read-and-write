from django.shortcuts import render
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from book import serializers
from book.models import Book
from book.permissions import IsOwner, IsOwnerOrAdmin
from like.models import Favorite
from like.serializers import LikeUserSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.BookListSerializer
        elif self.action in ('create', 'update', 'partial_update'):
            return serializers.BookCreateUpdateSerializer
        else:
            return serializers.BookDetailSerializer

    def get_permissions(self):
        if self.action == 'destroy':
            return [IsOwnerOrAdmin(), ]
        elif self.action in ('update', 'partial_update'):
            return [IsOwner(), ]
        return [permissions.IsAuthenticatedOrReadOnly(), ]

    @action(['GET'], detail=True)
    def likes(self, request, pk):
        book = self.get_object()
        likes = book.likes.all()
        serializer = LikeUserSerializer(instance=likes, many=True)
        return Response(serializer.data, status=200)

    @action(['POST', 'DELETE'], detail=True)
    def favorites(self, request, pk):
        book = self.get_object()
        user = request.user
        favorite = user.favorites.filter(book=book)

        if request.method == 'POST':
            if favorite.exists():
                return Response({'msg': 'Already in Mylibrary'}, status=400)
            Favorite.objects.create(owner=user, book=book)
            return Response({'msg': 'Added to Mylibrary'}, status=201)







