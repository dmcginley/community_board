# forms.py
from django import forms
from .models import NavbarSettings, HeroSettings, WebsiteSettings


class WebsiteSettingsForm(forms.ModelForm):
    class Meta:
        model = WebsiteSettings
        fields = ['primary_color', 'secondary_color', 'button_color', 'button_hover_color',
                  'button_text_color', 'button_hover_text_color']


        widgets = {
            'primary_color': forms.TextInput(attrs={'type': 'color'}),  # Adds a color picker
            'secondary_color': forms.TextInput(attrs={'type': 'color'}),  # Adds a color picker
            'button_color': forms.TextInput(attrs={'type': 'color'}),  # Adds a color picker
            'button_text_color': forms.TextInput(attrs={'type': 'color'}),  # Adds a color picker
            'button_hover_color': forms.TextInput(attrs={'type': 'color'}),  # Adds a color picker
            'button_hover_text_color': forms.TextInput(attrs={'type': 'color'}),  # Adds a color picker
        }

        

class NavbarSettingsForm(forms.ModelForm):
    class Meta:
        model = NavbarSettings
        fields = ['site_title', 'logo', 'alt_text']

        labels = {
            'site_title': 'Site Title',
            'logo': 'Site Logo',
            'alt_text': 'Logo alt text'
        }


class HeroSettingsForm(forms.ModelForm):
    class Meta:
        model = HeroSettings
        fields = ['hero_active', 'hero_image', 'text_color', 'bg_color', 'h1_text',
                  'sub_text', 'button_one_text', 'button_one_link',
                  'button_two_text', 'button_two_link', 'featured_active',
                  'featured_one_icon', 'featured_one_link', 'featured_two_icon',
                  'featured_two_link', 'featured_three_icon', 'featured_three_link']


        labels = {
            'hero_active': 'Activeate Hero Section',
            'bg_color': 'Background Color',
            'featured_active': 'Activate Featured Section',
        }


        widgets = {
            'bg_color': forms.TextInput(attrs={'type': 'color'}),  # Adds a color picker
            'text_color': forms.TextInput(attrs={'type': 'color'}),  # Adds a color picker
        }