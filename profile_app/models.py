from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Links Profile to a User
    email = models.EmailField(max_length=254, blank=True)  # Optional email field
    bio = models.TextField(max_length=500, blank=True)  # Optional bio field
    location = models.CharField(max_length=100, blank=True)  # Optional location field
    birth_date = models.DateField(null=True, blank=True)  # Optional birth date field
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/profile_image.webp', blank=True, null=True)  # Optional profile picture
    occupation = models.CharField(max_length=100, blank=True)  # Optional profection field
    last_seen = models.DateTimeField(default=timezone.now)  # Track last seen time, default to current time

    def __str__(self):
        return self.user.username