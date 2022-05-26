import json

import requests

from celery import shared_task

from django.contrib.auth.tokens import default_token_generator as token
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from django.contrib.auth import get_user_model
User = get_user_model()


@shared_task
def city_search(request: str) -> str:
    token = 'a907a918a9546d'
    url = f'https://ipinfo.io/{request}?token={token}'
    response = requests.get(url).text
    try:
        a = json.loads(response)['city']
    except Exception:
        a = 'Armenia'
    return a


@shared_task
def send_activation_notification(pk):
    user = User.objects.get(pk=pk)
    context = {
        'user': user,
        'domain': 'localhost:8000',
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token.make_token(user),
    }
    messages = render_to_string(
        'email/activ_body.txt',
        context)
    email = EmailMessage(
        'Veryfi email',
        messages,
        to=[user.email],
    )
    return email.send()