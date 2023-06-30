from rest_framework import viewsets
from .models import Book, Chapter
from .serializers import BookSerializer, ChapterSerializer


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
