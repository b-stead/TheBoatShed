from pyexpat import model
from django.db import models
from tkinter import CASCADE
from tabnanny import verbose
from django.conf import settings
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User


# Create your models here.
GENDER = (
    (None, 'Choose your gender'),
    ('male', 'male'),
    ('female', 'female'),
    ('other', 'other'),
)

DISCIPLINE = (
    (None, 'Choose your primary discipline'),
    ('kayak', 'kayak'),
    ('canoe', 'canoe'),
    ('sup', 'sup'),
    ('ski', 'ski'),
)

CLASSIFICATION = (
    ('able-bodied', 'able-bodied'),
    ('para-canoe', 'para-canoe'),
)

WATER_COND = (
    ('calm', 'calm'),
    ('ripples', 'ripples'),
    ('slight', 'slight'),
    ('rough', 'rough'),
)

BOATTYPE = (
    (None, 'Choose a boat'),
    ('k1', 'k1'),
    ('k2', 'k2'),
    ('k4', 'k4'),
    ('c1', 'c1'),
    ('c2', 'c2'),
    ('c4', 'c2'),
    ('Vaa', 'Vaa'),
    ('sk1', 'sk1'),
    ('sk2', 'sk2'),
)

ACTIVE_STATUS = 0
INACTIVE_STATUS = 1

STATUS = (
    (ACTIVE_STATUS, "Active"),
    (INACTIVE_STATUS, "Inactive"),
)

class User(User):
    is_coach = models.BooleanField(default=False)
    is_athlete = models.BooleanField(default=False)
  
class Squad(models.Model):
    name = models.CharField(max_length=10, blank=True)

class Coach(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(1, "Name must be greater than 1 character")], null=True)
    email = models.EmailField(max_length=254, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    #squad = models.ForeignKey(Squad, on_delete=models.CASCADE, related_name='my_squad')
    USERNAME_FIELD = 'user'
    class Meta:
        verbose_name_plural = 'Coaches'

    def __str__(self):
        return self.name

class Athlete(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(1, "Name must be greater than 1 character")], null=True)
    dob = models.DateField(verbose_name="D.O.B", null=True)
    gender = models.CharField(max_length=6, choices=GENDER, verbose_name="gender", blank=True)
    discipline = models.CharField(max_length=6, choices=DISCIPLINE, verbose_name="discipline", blank=True)
    classification = models.CharField(max_length=12, choices=CLASSIFICATION, verbose_name="classification", blank=True)
    club = models.CharField(max_length=50, verbose_name="club", blank=True)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, related_name='my_coach')
    #squad = models.ForeignKey(Squad, on_delete=models.CASCADE, related_name='my_squad')
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta:
        verbose_name_plural = 'Athletes'

    def __str__(self):
        return self.name        



