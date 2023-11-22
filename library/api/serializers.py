from rest_framework import serializers

from books.models import Books


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = ('id', 'title', 'author', 'pub_date', 'isbn')
