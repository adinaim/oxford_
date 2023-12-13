from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model


User = get_user_model()


def send_activation_code(email, activation_code):
    activation_link = f'http://http://127.0.0.1:8000/api/account/activate/{activation_code}/'
    html_message = render_to_string(
        'account/index.html',
        {'activation_link': activation_link}
        )
    send_mail(
        'Активируйте ваш аккаунт!',
        '',
        settings.EMAIL_HOST_USER,
        [email],
        html_message=html_message,
        fail_silently=False   
    )


def send_change_password_code(email, code):

    html_message = render_to_string(
        'account/password_code_mail.html',
        {'code': code}
        )
    send_mail(
        'Сбросить пароль',
        '',
        settings.EMAIL_HOST_USER,
        [email],
        html_message=html_message,
        fail_silently=False   
    )