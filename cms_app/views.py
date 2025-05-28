from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpRequest
from user_visit.models import UserVisit
from django.utils.timezone import now
from django.utils import timezone
from datetime import timedelta

from cms_app.models import (
    NavbarSettings, HeroSettings,
    WebsiteSettings
    )

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from profile_app.models import User
from community_board_app.models import Category
from cms_app.forms import NavbarSettingsForm, HeroSettingsForm, WebsiteSettingsForm
from django.views import View
from django.urls import reverse
from django.db.models import Count



class CMSDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "cms_app/cms_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_view"] = self.request.resolver_match.view_name  # Get the current view name
        return context
    


@login_required
def cms_overview_view(request: HttpRequest):
    # If not authenticated, return 403 Forbidden
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You do not have permission to view this page.")

    if request.headers.get('HX-Request'):
        return render(request, 'cms_app/partials/cms_overview.html')

    return render(request, 'cms_app/cms_dashboard.html', {'current_view': 'cms_overview_view'})



# CMS settings view
def cms_view(request):
    # Check if the user is authenticated, otherwise return a 403 Forbidden response
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You do not have permission to view this page.")
    
    navbar_settings, created_navbar = NavbarSettings.objects.get_or_create(pk=1)
    hero_settings, created_hero = HeroSettings.objects.get_or_create(pk=1)
    website_settings, created_website = WebsiteSettings.objects.get_or_create(pk=1)

    if request.method == 'POST':
        navbar_form = NavbarSettingsForm(request.POST, request.FILES, instance=navbar_settings)
        hero_form = HeroSettingsForm(request.POST, request.FILES, instance=hero_settings)
        website_form = WebsiteSettingsForm(request.POST, request.FILES, instance=website_settings)

        if navbar_form.is_valid() and hero_form.is_valid() and website_form.is_valid():
            navbar_form.save()
            hero_form.save()
            website_form.save()

            if request.headers.get('HX-Request'):
                return render(request, 'cms_app/partials/cms_site_settings.html', {
                    'navbar_form': navbar_form,
                    'hero_form': hero_form,
                    'website_form': website_form
                })

            return redirect(reverse('cms_app:cms_dashboard'))

    else:
        navbar_form = NavbarSettingsForm(instance=navbar_settings)
        hero_form = HeroSettingsForm(instance=hero_settings)
        website_form = WebsiteSettingsForm(instance=website_settings)

    if request.headers.get('HX-Request'):
        return render(request, 'cms_app/partials/cms_site_settings.html', {
            'navbar_form': navbar_form,
            'hero_form': hero_form,
            'website_form': website_form
        })

    return render(request, 'cms_app/cms_dashboard.html', {
        'navbar_form': navbar_form,
        'hero_form': hero_form,
        'website_form': website_form,
        'current_view': 'cms_view'
    })



class CmsUsersView(LoginRequiredMixin, View):
    model = User
    paginate_by = 50 
    
    def get(self, request: HttpRequest):
        # Query all users with their related profiles
        users = User.objects.all().select_related('profile')

        # Get the current time
        now = timezone.now()

        # Check if the user is online
        for user in users:
            # Consider user online if their last_seen is within the last 5 minutes
            user.is_online = user.profile.last_seen and now - user.profile.last_seen < timedelta(minutes=5)

        # If it's an HTMX request, return only the partial template
        if request.headers.get('HX-Request'):
            return render(request, 'cms_app/partials/cms_users.html', {'users': users})

        # For normal requests, return the full dashboard template
        return render(request, 'cms_app/cms_dashboard.html', {
            'current_view': 'cms_users_view',
            'users': users,
        })


@login_required
def cms_categories_view(request: HttpRequest):
    # Annotate categories with the number of related posts
    categories = Category.objects.annotate(post_count=Count('posts'))

    # Check if the user is authenticated; if not, return 403 Forbidden
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You do not have permission to view this page.")

    # Handle HTMX requests by returning only the partial template
    if request.headers.get("HX-Request"):
        return render(request, "cms_app/partials/cms_categories.html", {"categories": categories})

    # For normal requests, render the full dashboard template
    return render(
        request,
        "cms_app/cms_dashboard.html",
        {
            "current_view": "cms_categories_view",
            "categories": categories
        }
    )
