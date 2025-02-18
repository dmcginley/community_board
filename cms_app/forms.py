# forms.py
from django import forms
from .models import NavbarSettings, HeroSettings

class NavbarSettingsForm(forms.ModelForm):
    class Meta:
        model = NavbarSettings
        fields = ['site_title', 'logo', 'alt_text']


class HeroSettingsForm(forms.ModelForm):
    class Meta:
        model = HeroSettings
        fields = ['hero_image', 'bg_color', 'h1_text', 'sub_text', 'button_one_text', 'button_one_link', 'button_two_text', 'button_two_link']
        widgets = {
            'bg_color': forms.TextInput(attrs={'type': 'color'}),  # Adds a color picker
        }