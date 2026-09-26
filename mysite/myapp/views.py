from urllib import request
from django.shortcuts import render
from .models import UserProfiles

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def user_profile_no(request):
    return render(request, 'user_profile.html', {'username': 'Гость'})

def user_profile(request, username):
    user = UserProfiles[username]
    return render(request, 'user_profile.html', {
        'username': user['username'],
        'age': user['age'],
        'city': user['city'],
        'ip_address': user['ip_address'],
        'about_me': user['about_me'],
    })

