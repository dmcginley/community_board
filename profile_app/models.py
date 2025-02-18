from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Links Profile to a User
    bio = models.TextField(max_length=500, blank=True)  # Optional bio field
    location = models.CharField(max_length=100, blank=True)  # Optional location field
    birth_date = models.DateField(null=True, blank=True)  # Optional birth date field
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Optional profile picture

    def __str__(self):
        return f'{self.user.username} Profile'