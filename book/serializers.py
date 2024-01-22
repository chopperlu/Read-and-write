from rest_framework import serializers

from book.models import Book
from comment.serializers import CommentSerializer


class BookListSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    category_name = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = Book
        fields = ('id', 'title', 'preview', 'owner', 'owner_username', 'author', 'category', 'category_name', 'genre', 'description')

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        user = self.context['request'].user
        if user.is_authenticated:
            repr['is_liked'] = user.likes.filter(book=instance).exists()
        return repr


class BookCreateUpdateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    class Meta:
        model = Book
        fields = '__all__'


class BookDetailSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Book
        fields = '__all__'


    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['comments_count'] = instance.comments.count()
        repr['comments'] = CommentSerializer(instance=instance.comments.all(), many=True).data
        repr['likes_count'] = instance.likes.count()
        user = self.context['request'].user
        if user.is_authenticated:
            repr['is_liked'] = user.likes.filter(book=instance).exists()
        return repr



# class CreateRatingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Rating
#         fields = ('id', 'star', 'book')
#
#
#     def create(self, validated_data):
#         rating = Rating.objects.update_or_create(
#
#         )



