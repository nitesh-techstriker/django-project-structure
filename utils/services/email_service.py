import os
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode
from utils.common import account_activation_token


def account_verification_email_send(email, user, forgetpassword_url):
    mail_subject = 'CHODIRECT: Verify your account.'
    message = render_to_string('email_verification.html', {
        'email': user.email,
        'domain': os.environ.get("API_URL"),
        'uid': urlsafe_base64_encode(force_bytes(user.id)),
        'token': account_activation_token.make_token(user),
        "forgetpassword": forgetpassword_url
    })
    to_email = email
    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()
