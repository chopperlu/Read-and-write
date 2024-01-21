from django.db import models
from book.models import Book


class Like(models.Model):
    owner = models.ForeignKey('auth.User', related_name='likes', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ['owner', 'book']


class Favorite(models.Model):
    owner = models.ForeignKey('auth.User', related_name='favorites', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='favorites', on_delete=models.CASCADE)


    class Meta:
        unique_together = ['owner', 'book']
