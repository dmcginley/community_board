from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpRequest
from cms_app.models import NavbarSettings, HeroSettings
from profile_app.models import User
from cms_app.forms import NavbarSettingsForm, HeroSettingsForm
from django.views import View
from django.urls import reverse


class CMSDashboardView(TemplateView):
    template_name = "cms_app/cms_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_view"] = self.request.resolver_match.view_name  # Get the current view name
        return context
    


def cms_overview_view(request: HttpRequest):
    
    if request.headers.get('HX-Request'):
        return render(request, 'cms_app/partials/cms_overview.html')

    return render(request, 'cms_app/cms_dashboard.html', {'current_view': 'cms_overview_view'})

# CMS settings view
def cms_view(request):
    navbar_settings, created_navbar = NavbarSettings.objects.get_or_create(pk=1)
    hero_settings, created_hero = HeroSettings.objects.get_or_create(pk=1)

    if request.method == 'POST':
        navbar_form = NavbarSettingsForm(request.POST, request.FILES, instance=navbar_settings)
        hero_form = HeroSettingsForm(request.POST, request.FILES, instance=hero_settings)

        if navbar_form.is_valid() and hero_form.is_valid():
            navbar_form.save()
            hero_form.save()
            
            # Return only the partial template if HTMX request
            if request.headers.get('HX-Request'):
                return render(request, 'cms_app/partials/cms_site_settings.html', {
                    'navbar_form': navbar_form,
                    'hero_form': hero_form
                })

            return redirect(reverse('cms_app:cms_dashboard'))

    else:
        navbar_form = NavbarSettingsForm(instance=navbar_settings)
        hero_form = HeroSettingsForm(instance=hero_settings)

    # If HTMX, return only the partial content
    if request.headers.get('HX-Request'):
        return render(request, 'cms_app/partials/cms_site_settings.html', {
            'navbar_form': navbar_form,
            'hero_form': hero_form
        })

    # Otherwise, render the full page
    return render(request, 'cms_app/cms_dashboard.html', {
        'navbar_form': navbar_form,
        'hero_form': hero_form,
        'current_view': 'cms_view'
    })



class CmsUsersView(View):
    model = User

    def get(self, request: HttpRequest):
        users = User.objects.all().select_related('profile')  # Query users and related profile
        
        # If it's an HTMX request, return only the partial template
        if request.headers.get('HX-Request'):
            return render(request, 'cms_app/partials/cms_users.html', {'users': users})

        # For normal requests, return the full dashboard template
        return render(request, 'cms_app/cms_dashboard.html', {'current_view': 'cms_users_view', 'users': users})


def cms_categories_view(request: HttpRequest):
    
    if request.headers.get('HX-Request'):
        return render(request, 'cms_app/partials/cms_categories.html')

    return render(request, 'cms_app/cms_dashboard.html', {'current_view': 'cms_categories_view'})