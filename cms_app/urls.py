from django.urls import path
from .views import CmsUsersView,cms_overview_view, cms_view, cms_categories_view, CMSDashboardView

app_name = 'cms_app'

urlpatterns = [
    path("dashboard", cms_overview_view, name="cms_overview_view"),  # Correct name
    path('', CMSDashboardView.as_view(), name='cms_dashboard'),
    path('users', CmsUsersView.as_view(), name='cms_users_view'),
    path('settings', cms_view, name='cms_view'),
    path('categories', cms_categories_view, name='cms_categories_view'),
]