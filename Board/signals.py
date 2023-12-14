from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import UserResponse


@receiver(pre_save, sender=UserResponse)
def my_handler(instance):
    if instance.status:
        mail = instance.author.email
        send_mail(
            'Subject here',
            'Here is the message.',
            'host@mail.ru',
            [mail],
            fail_silently=False,
        )
    mail = instance.article.author.email
    send_mail(
        'Subject here',
        'Here is the message.',
        'host@mail.ru',
        [mail],
        fail_silently=False,
    )