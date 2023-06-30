from rest_framework import serializers
from .models import Book, Chapter


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'title')


class BookSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True,)

    class Meta:
        model = Book
        fields = ('id', 'title', 'chapters')
