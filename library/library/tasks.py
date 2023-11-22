from django.core.mail import send_mail

from celery import shared_task


@shared_task()
def send_email(email):
    send_mail(
        'Поздравление',
        'Поздравляем с успешной регистрацией на сайте!)',
        'info@book.com',
        [email],
        fail_silently=False,
    )
