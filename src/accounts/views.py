import uuid
import sys

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from accounts.models import Token
# Create your views here.


def send_login_email(request):
    """TODO: Docstring for send_login_email.

    :request: TODO
    :returns: TODO

    """
    email = request.POST['email']
    uid = str(uuid.uuid4())
    Token.objects.create(email=email, uid=uid)
    print('saving uid', uid, 'for email', email, file=sys.stderr)
    url = request.build_absolute_uri(f'/accounts/login?uid={uid}/')
    send_mail(
            'Your login link for Superlisrts',
            f'Use this link to log in:\n\n{url}',
            'noreply@superlists',
            [email],
    )
    return render(request, 'accounts/login_email_sent.html')

def login(request):
    """TODO: Docstring for login.

    :request: TODO
    :returns: TODO

    """
    print('login view', file=sys.stderr)
    uid = request.GET.get('uid')
    user = authenticate(uid=uid)
    if user is not None:
        auth_login(request, user)
    return redirect('/')


def logout(request):
    """TODO: Docstring for logout.

    :request: TODO
    :returns: TODO

    """
    auth_logout(request)
    return redirect('/')
