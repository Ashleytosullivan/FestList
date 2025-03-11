from django.shortcuts import render
from .models import PlaylistPost

def home(request):
    posts = PlaylistPost.objects.all()  # Fetch all posts
    return render(request, 'home.html', {'posts': posts})
