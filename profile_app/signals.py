from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.utils import timezone
from user_visit.models import UserVisit
from django.utils.timezone import now

# Automatically create a profile when a user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Automatically save the profile when the user is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# TODO: not reall in use
@receiver(user_logged_in)
def update_last_seen(sender, request, user, **kwargs):
    # Get or create the user's profile
    profile, created = Profile.objects.get_or_create(user=user)
    
    # Update the 'last_seen' field with the current time
    profile.last_logged_in = timezone.now()
    
    # Save the profile
    profile.save()

    # Optionally, log it for debugging purposes
    print(f"Last seen for {user.username} updated to {profile.last_seen}")



@receiver(user_logged_out)
def update_last_seen_on_logout(sender, request, user, **kwargs):
    # Get or create the user's profile
    profile, created = Profile.objects.get_or_create(user=user)
    
    # Update the 'last_seen' field with the current time
    profile.last_seen = timezone.now()
    
    # Save the profile
    profile.save()

    # Optionally, log it for debugging purposes
    print(f"Last seen for {user.username} updated to {profile.last_seen}")


# TODO: Implement a signal to log user visits
@receiver(user_logged_in)
def log_user_visit(sender, request, user, **kwargs):
    if user.is_authenticated:
        # Log the visit for the authenticated user
        UserVisit.objects.create(user=user)  # Don't explicitly pass 'visited_at'
        print(f"Logged visit for {user.username} at {now()}")