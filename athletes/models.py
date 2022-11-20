from django.db import models
from datetime import datetime
from django.core.validators import MinLengthValidator
from django.conf import settings
from django.utils import timezone
from profiles.models import Coach, Athlete
from django.utils.translation import gettext as _
# Create your models here.
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

METRIC_CHOICES = (
    ('Overall Feeling', 'feeling'),
    ('Pulse', 'pulse'),
    ('Sickness', 'sickness'),
    ('Sleep Hours', 'sleep_hours'),
    ('Sleep Qualilty', 'sleep qualilty'),
    ('Soreness', 'soreness'),
    ('Stress', 'stress'),
    ('Weight Kilograms', 'weight_kg'),
    ('Yesterday\'s Training', 'yesterdays_training'),
    ('Fatigue', 'fatigue'),
    ('Menstruation', 'menstruation'),
    ('Injury', 'injury'),

)

mapping = dict(Sickness=1.428571429, 
                Fatigue=1.428571429,
                Menstruation=1.428571429,
                SleepQual=1.428571429,
                Stress=1.428571429,
                Training=2.5,
                Feeling=1,
                Pulse=1,
                Sleep_Hours=1,
                Soreness=1,
                Weight_Kg=1,
                Injury=1)

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

class Sport(StandardMetadata):
    """Sport model.
       A farily simple model to handle categorizing of teams into sports."""
    name=models.CharField(_('name'), max_length=100)
    slug=models.SlugField(_('slug'), unique=True) 

    def __unicode__(self):
        return self.name

class BoatType(models.Model):
    name = models.CharField(max_length=4, choices=BOATTYPE, verbose_name="boat", blank=True)
    
    def __str__(self):
        return self.name


class Venue(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(1, "Venue must be greater than 1 character")], null=True)       
    
    def __str__(self):
        return self.name

class Session(StandardMetadata):
    uid = models.CharField(max_length=50, validators=[MinLengthValidator(1,"AthleteInitials-Date dd/mm/yyy- session")], null=True)
    created_at = models.DateTimeField(default=timezone.now)
    crew=models.CharField(max_length=20, validators=[MinLengthValidator(1, "Crew must be greater than 1 character")], null=True)
    session_name=models.CharField(max_length=20, null=True)
    session_date = models.DateTimeField(default=timezone.now)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, null=True)
    boat = models.ForeignKey(BoatType, on_delete=models.CASCADE, null=True)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, null=True)
    conditions = models.CharField(max_length=4, choices=WATER_COND, verbose_name="conditions", blank=True)
    def __str__(self):
        return self.uid
    

class Effort(StandardMetadata):
    number = models.PositiveIntegerField(verbose_name="number")
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    length = models.PositiveIntegerField(verbose_name="Distance(m)")
    time = models.PositiveIntegerField(verbose_name="Time(s)")


class Metrics(StandardMetadata):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    date = models.DateTimeField()
    metric = models.CharField(max_length=25, choices=METRIC_CHOICES)
    value = models.FloatField()
    score = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return f"{self.metric}"

    def save(self, *args, **kwargs):
        score = None
        if self.metric ==('Sickness', 'Fatigue', 'Menstruation', 'Stress', 'Sleep Quality'):
            conv = 1.428571429
        if self.metric == 'Yesterday\'s Training':
            conv = 2.5
        else:
            conv = 1
        self.score = conv * self.total
        super().save(*args, **kwargs)


