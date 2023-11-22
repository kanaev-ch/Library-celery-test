from rest_framework import viewsets

from books.models import Books
from .serializers import BookSerializer


class BookViewset(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    pagination_class = None
