from django.shortcuts import render, redirect
from cms_app.models import NavbarSettings, HeroSettings
from cms_app.forms import NavbarSettingsForm, HeroSettingsForm

def cms_view(request):
    # Get or create NavbarSettings and HeroSettings instances
    navbar_settings, created_navbar = NavbarSettings.objects.get_or_create(pk=1)
    hero_settings, created_hero = HeroSettings.objects.get_or_create(pk=1)

    if request.method == 'POST':
        navbar_form = NavbarSettingsForm(request.POST, request.FILES, instance=navbar_settings)
        hero_form = HeroSettingsForm(request.POST, request.FILES, instance=hero_settings)

        if navbar_form.is_valid() and hero_form.is_valid():
            navbar_form.save()
            hero_form.save()
            return redirect('cms_app:cms_view')  # Redirect after saving

    else:
        navbar_form = NavbarSettingsForm(instance=navbar_settings)
        hero_form = HeroSettingsForm(instance=hero_settings)

    return render(request, 'cms_app/cms_form.html', {
        'navbar_form': navbar_form,
        'hero_form': hero_form
    })


def cms_users_view(request):
    return render(request, 'cms_app/cms_users.html')
    