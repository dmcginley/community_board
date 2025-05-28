from .models import NavbarSettings, WebsiteSettings

def navbar_settings(request):
    settings = NavbarSettings.objects.first()
    
    return {
        'navbar_title': settings.site_title if settings else "My Site",
        'navbar_logo': settings.logo.url if settings and settings.logo else None,
        'navbar_alt_text': settings.alt_text if settings else None,

    }


def website_settings(request):
    settings = WebsiteSettings.objects.first()  # Fetch the first settings instance

    # Provide default values if no settings are available
    return {
        'primary_color': settings.primary_color if settings else "#000000",
        'secondary_color': settings.secondary_color if settings else "#ffffff",
        'button_color': settings.button_color if settings else "#007bff",  # Default for button color
        'button_hover_color': settings.button_hover_color if settings else "#0056b3",  # Default for button hover color
        'button_text_color': settings.button_text_color if settings else "#ffffff",  # Default button text color
        'button_hover_text_color': settings.button_hover_text_color if settings else "#ffffff",  # Default button hover text color
    }