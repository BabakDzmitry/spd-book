from rest_framework.serializers import ModelSerializer

from store.models import Book


class BookSerializer(ModelSerializer):
    """Сериалайзер для книг"""
    class Meta:
        model = Book
        fields = '__all__'