from django.shortcuts import render
from rest_framework import generics, permissions

from book.models import Book


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.BookListSerializer
        return serializers.BookCreateUpdateSerializer
