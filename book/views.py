from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from book import serializers
from book.models import Book
from book.permissions import IsOwner, IsOwnerOrAdmin
from like.models import  Mylibrary
from like.serializers import LikeUserSerializer


class StandartResultPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page'

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    pagination_class = StandartResultPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('title', 'description')
    filterset_fields = ('owner', 'category')

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
    def mylibraries(self, request, pk):
        book = self.get_object()
        user = request.user
        mylibrary = user.mylibraries.filter(book=book)

        if request.method == 'POST':
            if mylibrary.exists():
                return Response({'msg': 'Already in Mylibrary'}, status=400)
            Mylibrary.objects.create(owner=user, book=book)
            return Response({'msg': 'Added to Mylibrary'}, status=201)


        if mylibrary.exists():
            mylibrary.delete()
            return Response({'msg': 'Deleted from Mylibrary'}, status=204)
        return Response({'msg': 'Mylibrary Not Found'}, status=404)





