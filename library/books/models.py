from django.db import models


class Books(models.Model):
    title = models.CharField(
        verbose_name='Название книги',
        max_length=256,
        help_text='Укажите название книги'
    )
    author = models.CharField(
        verbose_name='Имя автора книги',
        max_length=256,
        help_text='Укажите автора книги'
    )
    pub_date = models.DateField(
        verbose_name='Дата публикации',
        help_text='Укажите дату публикации книги'
    )
    isbn = models.PositiveBigIntegerField(
        verbose_name='ISBN книги',
        help_text='Укажите ISBN книги',
        unique=True,
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-pub_date']
