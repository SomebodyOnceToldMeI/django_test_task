from django.shortcuts import render

import json

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def create_post(request):
    return HttpResponse('Create post')

def like_post(request):
    return HttpResponse('Like post')

def unlike_post(request):
    return HttpResponse('Unlike post')

def signup_user(request):
    payload = json.loads(request.body)
    try:
        user = User.objects.get(username=payload['login'])
        return HttpResponse('User is already registered')
    except:
        user = User(username=payload['login'])
        user.set_password(payload['password'])
        user.save()
        return HttpResponse('Signup user')


def login_user(request):
    payload = json.loads(request.body)
    user = authenticate(username=payload['login'], password=payload['password'])
    if user:
        return HttpResponse('Login user')
    else:
        return HttpResponse('Authentication failed.')