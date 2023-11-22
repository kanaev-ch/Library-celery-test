from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(
        max_length=254,
        unique=True,
        blank=False,
        verbose_name='email'
    )
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=254,
        unique=True,
        blank=False,
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата регистрации'
    )

    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-pub_date']
