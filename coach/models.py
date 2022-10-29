from tkinter import CASCADE
from tkinter.tix import Tree
from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator
from django.forms import DateField
from django.utils import timezone
from django.forms.widgets import DateInput
from datetime import datetime, timedelta
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
             
#setup for athlete profiles & forms , is there a better DRY version??
GENDER = (
    (None, 'Choose your gender'),
    ('0', 'male'),
    ('1', 'female'),
    ('3', 'other'),
)

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

WATER_COND = (
    ('0', 'calm'),
    ('1', 'ripples'),
    ('2', 'slight'),
    ('3', 'rough'),
)

BOATTYPE = (
    (None, 'Choose a boat'),
    ('1', 'k1'),
    ('2', 'k2'),
    ('3', 'k4'),
    ('4', 'c1'),
    ('5', 'c2'),
    ('6', 'c2'),
    ('7', 'Va\'a'),
    ('8', 'sup'),
)

SEAT_POSITION = (

    ('0', 'First'),
    ('1', 'Second'),
    ('2', 'Third'),
    ('3', 'Fourth'),
)



class StandardMetadata(models.Model):
    """
    A basic (abstract) model for metadata.
    
	Subclass new models from 'StandardMetadata' instead of 'models.Model'.
    """
    created = models.DateTimeField(default=datetime.now, editable=False)
    updated = models.DateTimeField(default=datetime.now, editable=False)
    
    class Meta:
        abstract = True
    
    def save(self, *args, **kwargs):
        self.updated = datetime.now()
        super(StandardMetadata, self).save(*args, **kwargs)

class User(AbstractUser):
    is_athlete = models.BooleanField(default=False)
    is_coach = models.BooleanField(default=False)

class Sport(StandardMetadata):
    """Sport model.
       A farily simple model to handle categorizing of teams into sports."""
    name=models.CharField(_('name'), max_length=100)
    slug=models.SlugField(_('slug'), unique=True) 

    def __unicode__(self):
        return self.name

class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50, validators=[MinLengthValidator(1, "Name must be greater than 1 character")], null=True)
    def __str__(self):
        return self.name

class Athlete(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50, validators=[MinLengthValidator(1, "Name must be greater than 1 character")], null=True)
    dob = models.DateField(verbose_name="D.O.B", null=True)
    gender = models.CharField(max_length=6, choices=GENDER, verbose_name="gender", blank=True)
    discipline = models.CharField(max_length=6, choices=DISCIPLINE, verbose_name="discipline", blank=True)
    classification = models.CharField(max_length=12, choices=CLASSIFICATION, verbose_name="classification", blank=True)
    club = models.CharField(max_length=50, verbose_name="club", blank=True)
    coach = models.ManyToManyField('Coach', through='Squads')
    def __str__(self):
        return self.name


class Squads(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(1, "Name must be greater than 1 character")], null=True)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class BoatType(models.Model):
    name = models.CharField(max_length=4, choices=BOATTYPE, verbose_name="boat", blank=True)
    
    def __str__(self):
        return self.name

class Venue(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(1, "Venue must be greater than 1 character")], null=True)       
    
    def __str__(self):
        return self.name

class Session(models.Model):
    uid = models.CharField(max_length=50, validators=[MinLengthValidator(1,"AthleteInitials-Date dd/mm/yyy- session")], null=True)
    created_at = models.DateTimeField(default=timezone.now)
    crew=models.CharField(max_length=20, validators=[MinLengthValidator(1, "Crew must be greater than 1 character")], null=True)
    session_name=models.CharField(max_length=20, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    session_date = models.DateTimeField(default=timezone.now)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    boat = models.ForeignKey(BoatType, on_delete=models.CASCADE, null=True)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.uid
    

class Effort(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    length = models.PositiveIntegerField(verbose_name="Distance(m)")
    time = models.PositiveIntegerField(verbose_name="Time(s)")
