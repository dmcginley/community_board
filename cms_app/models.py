from django.db import models

class NavbarSettings(models.Model):
    site_title = models.CharField(max_length=255, default="My Site")
    logo = models.FileField(upload_to='navbar/', blank=True, null=True)
    alt_text = models.CharField(max_length=255, blank=True, null=True)  # Alt text for the logo
    def __str__(self):
        return "Navbar Settings"

    class Meta:
        verbose_name_plural = "Navbar Settings"


class HeroSettings(models.Model):
    hero_image = models.FileField(upload_to='images/', blank=True, null=True)
    bg_color = models.CharField(max_length=7, default="#111827") # Default color is a dark blue
    button_one_text = models.CharField(max_length=255, blank=True, null=True)
    button_one_link = models.CharField(max_length=255, blank=True, null=True)
    button_two_text = models.CharField(max_length=255, blank=True, null=True)
    button_two_link = models.CharField(max_length=255, blank=True, null=True)
    h1_text = models.CharField(max_length=255, blank=True, null=True)
    sub_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "Hero Section Settings"

    class Meta:
        verbose_name_plural = "Hero Settings"