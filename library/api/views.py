from rest_framework import viewsets

from books.models import Books
from users.models import User
from .serializers import BookSerializer, UserSerializer


class BookViewset(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class UserViewset(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    queryset = User.objects.all()
    serializer_class = UserSerializer
