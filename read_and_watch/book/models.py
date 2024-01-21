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

