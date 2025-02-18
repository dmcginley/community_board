from django.urls import path
from . import views
from .views import cms_view, cms_users_view
app_name = 'cms_app'

urlpatterns = [
    path('', cms_view, name='cms_view'),
    path('users', cms_users_view, name='cms_users_view'),
]