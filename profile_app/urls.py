from django.urls import path
from .views import profile, edit_profile

app_name = 'profile_app'

urlpatterns = [
    path('', profile, name='profile'),
    path('edit/', edit_profile, name='edit_profile'),
]