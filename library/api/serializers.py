from rest_framework import serializers
# from django.core.mail import send_mail

from books.models import Books
from users.models import User
from library.tasks import send_email


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = ('id', 'title', 'author', 'pub_date', 'isbn')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'signup_date')

    # def send_email(self, email):
    #     send_mail(
    #         'Поздравление',
    #         'Поздравляем с успешной решистрацией на сайте!)',
    #         'info@book.com',
    #         [email],
    #         fail_silently=False,
    #     )

    def create(self, validated_data):
        email = self.initial_data['email']
        # self.send_email(email)
        send_email.delay(email)
        user = User.objects.create(**validated_data)
        return user
