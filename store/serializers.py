from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from store.models import Book, UserBookRelation


class BookSerializer(ModelSerializer):
    """Сериалайзер для книг"""
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ('id', 'name', 'price', 'author_name')

    def get_likes_count(self, instance):
        return UserBookRelation.objects.filter(book=instance, like=True).count()


class UserBookRelationSerializer(ModelSerializer):
    """Сериалайзер для статуса книг"""

    class Meta:
        model = UserBookRelation
        fields = ('book', 'like', 'in_bookmarks', 'rate')
