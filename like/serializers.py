from rest_framework import serializers

from like.models import Like, Mylibrary


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    owner_username = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Like
        fields = '__all__'
    def validate(self, attrs):
        user = self.context['request'].user
        book = attrs['book']
        if user.likes.filter(book=book).exists():
            raise serializers.ValidationError('You already liked this book!')
        return attrs



class LikeUserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    owner_username = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        exclude = ('book', )

class MylibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Mylibrary
        fields = ('id', 'book')

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['book_title'] = instance.book.title
        preview = instance.book.preview
        repr['book_preview'] = preview.url if preview else None
        return repr