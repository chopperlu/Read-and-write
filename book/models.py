from django.contrib.auth.models import User
from django.db import models

from category.models import Category


class Book(models.Model):
    owner = models.ForeignKey('auth.User', related_name='book', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=150)
    genre = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(Category, related_name='book', on_delete=models.SET_NULL, null=True)
    first_published = models.DateField()
    publisher = models.CharField(max_length=50, blank=True)
    preview = models.ImageField(upload_to='images', null=True)
    description = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    book_file = models.FileField(upload_to='books/', blank=False)


    def __str__(self):
        return f'{self.owner} - {self.title}'

    class Meta:
        ordering = ('created_at',)


class UserBookRelation(models.Model):
    RATE_CHOICES = (
        (1, 'ok'),
        (2, 'fine'),
        (3, 'Good'),
        (4, 'Amazing'),
        (5, 'Incredible')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)

    def __str__(self):
        return f'{self.user} - {self.book} - {self.rate}'