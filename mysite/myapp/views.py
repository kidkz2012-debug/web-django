from urllib import request
from django.shortcuts import render
from .models import UserProfiles

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def user_profile(request, username):
    user = UserProfiles.get(username)

    if user is None:
        return render(request, 'user_profile.html', {
            'username': 'Пользователь не найден',
            'age': 'Неизвестно',
            'city': 'Неизвестно',
            'ip_address': 'Неизвестно',
            'about_me': 'Неизвестно',
        })

    return render(request, 'user_profile.html', {
        'username': user['username'],
        'age': user['age'],
        'city': user['city'],
        'ip_address': user['ip_address'],
        'about_me': user['about_me'],
    })
