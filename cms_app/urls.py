from django.urls import path
from .views import CmsUsersView,cms_view, cms_categories_view, CMSDashboardView

app_name = 'cms_app'

urlpatterns = [
    path('', CMSDashboardView.as_view(), name='cms_dashboard'),
    path('settings', cms_view, name='cms_view'),
    path('users', CmsUsersView.as_view(), name='cms_users_view'),
    path('categories', cms_categories_view, name='cms_categories_view'),
]