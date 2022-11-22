from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _
from django.core.validators import MinLengthValidator

# Create your models here.

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
    username = models.CharField(max_length = 20)

    def __str__(self):
        return self.username
    

class AthleteDemo(models.Model):
    class Gender(models.TextChoices):
        MEN = 'MEN', 'Men'
        WOMEN = 'WOMEN', 'Women'
    gender = models.CharField(max_length=5, choices= Gender.choices,
        default=Gender.MEN)

    username = models.CharField(max_length = 20)
    date_of_birth = models.DateField(null=True)
    coach = models.ForeignKey(CoachDemo, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username