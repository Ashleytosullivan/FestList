from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.contrib.auth.models import User  # For linking posts to users

class PlaylistPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    spotify_url = models.URLField()  # To store Spotify playlist links
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to user
    tags = models.CharField(max_length=100, blank=True)  # Comma-separated tags

    def __str__(self):
        return self.title