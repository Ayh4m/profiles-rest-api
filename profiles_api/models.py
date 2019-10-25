from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings

from . import managers


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = managers.UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        """Return string representation of the user object"""
        return self.email

    def get_full_name(self):
        """Returns the first_name plus the last_name, with a space in between"""
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Returns the short name for the user"""
        return self.first_name


class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model's object as string"""
        return self.status_text
