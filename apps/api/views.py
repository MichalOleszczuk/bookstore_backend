from rest_framework import viewsets

from apps.core.models import Book
from apps.api.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('publication_date')
    serializer_class = BookSerializer
