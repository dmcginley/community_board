from django.contrib import admin
from .models import NavbarSettings, WebsiteSettings

@admin.register(NavbarSettings)
class NavbarSettingsAdmin(admin.ModelAdmin):
    # Ensure only one instance can be created
    def has_add_permission(self, request):
        return not NavbarSettings.objects.exists()
    


@admin.register(WebsiteSettings)
class WebsiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not WebsiteSettings.objects.exists()
