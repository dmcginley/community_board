from django.db import models
from django.core.cache import cache  # Import cache
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User

class WebsiteSettings(models.Model):
    primary_color = models.CharField(max_length=7, default="#3498db")  # Hex color
    secondary_color = models.CharField(max_length=7, default="#2c3e50")  # Hex color
    
    button_color = models.CharField(max_length=7, default="#3498db")  # Hex color
    button_text_color = models.CharField(max_length=7, default="#ffffff")  # Hex color
    button_hover_color = models.CharField(max_length=7, default="#2980b9")  # Hex color
    button_hover_text_color = models.CharField(max_length=7, default="#ffffff")  # Hex color

    def save(self, *args, **kwargs):
        if WebsiteSettings.objects.exists() and not self.pk:
            raise ValidationError("Only one instance of WebsiteSettings is allowed.")
        super().save(*args, **kwargs)
        cache.clear()  # Clear cache to apply changes instantly

    def __str__(self):
        return "Website Settings"

    class Meta:
        verbose_name = "Website Setting"
        verbose_name_plural = "Website Settings"

class NavbarSettings(models.Model):
    site_title = models.CharField(max_length=255, default="My Site")
    logo = models.FileField(upload_to='navbar_icon/', blank=True, null=True)
    alt_text = models.CharField(max_length=255, blank=True, null=True)  # Alt text for the logo
    def __str__(self):
        return "Navbar Settings"

    class Meta:
        verbose_name_plural = "Navbar Settings"


class HeroSettings(models.Model):
    hero_active = models.BooleanField(default=False)
    hero_image = models.FileField(upload_to='images/', blank=True, null=True)
    text_color = models.CharField(max_length=7, default="#ffffff")  # Default color is white
    bg_color = models.CharField(max_length=7, default="#111827") # Default color is a dark blue
    button_one_text = models.CharField(max_length=255, blank=True, null=True)
    button_one_link = models.CharField(max_length=255, blank=True, null=True)
    button_two_text = models.CharField(max_length=255, blank=True, null=True)
    button_two_link = models.CharField(max_length=255, blank=True, null=True)
    h1_text = models.CharField(max_length=255, blank=True, null=True)
    sub_text = models.CharField(max_length=255, blank=True, null=True)

    featured_active = models.BooleanField(default=False)
    featured_one_icon = models.FileField(upload_to='icons/', blank=True, null=True)
    featured_one_link = models.CharField(max_length=255, blank=True, null=True)
    featured_two_icon = models.FileField(upload_to='icons/', blank=True, null=True)
    featured_two_link = models.CharField(max_length=255, blank=True, null=True)
    featured_three_icon = models.FileField(upload_to='icons/', blank=True, null=True)
    featured_three_link = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "Hero Section Settings"

    class Meta:
        verbose_name_plural = "Hero Settings"
