# Generated by Django 3.2 on 2023-11-22 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=254, unique=True, verbose_name='Имя пользователя'),
        ),
    ]
