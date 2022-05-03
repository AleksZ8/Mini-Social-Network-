import requests
import json
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator as \
    token


def send_activation_notification(request, user):
    context = {
        'user': user,
        'domain': 'localhost:8000',
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token.make_token(user),
    }
    messages = render_to_string(
        'email/activ_body.txt',
        context)
    subject = render_to_string(
        'email/activ_sub.txt',
        context)
    email = EmailMessage(
        'Veryfi email',
        messages,
        to=[user.email],
    )
    email.send()


def city_search(request: str) -> str:
    token = 'a907a918a9546d'
    url = f'https://ipinfo.io/{request}?token={token}'
    response = requests.get(url).text
    try:
        a = json.loads(response)['city']
    except KeyError:
        a = 'Armenia'
    return a
