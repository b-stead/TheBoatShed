#https://dev.to/earthcomfy/getting-started-custom-user-model-5hc
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


from .managers import CustomUserManager

"""
class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    is_coach = models.BooleanField(default=True)
    is_athlete = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = CustomUserManager()

    def __str__(self):
        return self.email
"""



     