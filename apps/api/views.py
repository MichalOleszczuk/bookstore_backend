from rest_framework import viewsets

from apps.core.models import Book
from apps.api.serializers import BookSerializer, UserSerializer
from rest_framework.generics import views
from rest_framework.response import Response


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('publication_date')
    serializer_class = BookSerializer


class CheckAuthView(views.APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
