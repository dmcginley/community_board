from .models import NavbarSettings

def navbar_settings(request):
    settings = NavbarSettings.objects.first()
    
    return {
        'navbar_title': settings.site_title if settings else "My Site",
        'navbar_logo': settings.logo.url if settings and settings.logo else None,
        'navbar_alt_text': settings.alt_text if settings else None,
    }
