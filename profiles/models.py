from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _
from django.core.validators import MinLengthValidator
# Create your models here.

class User(AbstractUser):
    is_athlete = models.BooleanField(default=False)
    is_coach= models.BooleanField(default=False)
    is_admin= models.BooleanField(default=False)

class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    date_of_birth = models.DateField(null=True)
    def __str__(self):
        return self.username
@receiver(post_save, sender=User)
def create_coach_user_profile(sender, instance, created, **kwargs):
    if created:
        Coach.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_coach_profile(sender, instance, **kwargs):
    instance.coach.save()
    

class Team(models.Model):
    coach = models.ManyToManyField(Coach)
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Athlete(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    date_of_birth = models.DateField(null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username

@receiver(post_save, sender=User)
def create_athlete_user_profile(sender, instance, created, **kwargs):
    if created:
        Athlete.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_coach_profile(sender, instance, **kwargs):
    instance.athlete.save()

