from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _
from django.core.validators import MinLengthValidator
from django_resized import ResizedImageField
from datetime import datetime

DISCIPLINE = (
    (None, 'Choose your primary discipline'),
    ('0', 'kayak'),
    ('1', 'canoe'),
    ('2', 'sup'),
)

CLASSIFICATION = (
    ('0', 'able-bodied'),
    ('1', 'para-canoe'),
)

class TeamDemo(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    athletes = models.ManyToManyField('AthleteDemo', related_name="teams")
    coaches = models.ManyToManyField('CoachDemo', related_name="teams")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class CoachDemo(models.Model):
    name = models.CharField(max_length = 20)
    bio = models.CharField(max_length=400, null=True, blank=True)
    profile_pic = ResizedImageField(size=[50, 80], quality=100, upload_to="coachdemo", default=None, null=True, blank=True)

    def __str__(self):
        return self.user_name
    

class AthleteDemo(models.Model):
    class Gender(models.TextChoices):
        MEN = '0', 'Male'
        WOMEN = '1', 'Female'
    gender = models.CharField(choices= Gender.choices, max_length = 7)

    name = models.CharField(max_length = 20)
    date_of_birth = models.DateField(null=True)
    coach = models.ForeignKey(CoachDemo, on_delete=models.CASCADE, null=True)
    discipline = models.CharField(max_length=6, choices=DISCIPLINE, verbose_name="discipline", blank=True)
    classification = models.CharField(max_length=12, choices=CLASSIFICATION, verbose_name="classification", blank=True)
    club = models.CharField(max_length=50, verbose_name="club", blank=True)
    profile_pic = ResizedImageField(size=[50, 80], quality=100, upload_to="athlete", default=None, null=True, blank=True)
    bio = models.CharField(max_length=400, null=True, blank=True)
    
    @property
    def age(self):
        return int((datetime.now().date() - self.DOB).days / 365.25)
    def __str__(self):
        return self.user_name