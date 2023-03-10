from django.db import models
from uploader.models import Vbo
from profiles.models import Athlete
# Create your models here.

class SessionPeaks(models.Model):
    SESSION_TYPES = (
        ('TRAINING', 'Training'),
        ('STANDALONE', 'Standalone Effort'),
        ('RACE', 'Racing'),
        # add other session types as needed
    )
    session_type = models.CharField(max_length=10, choices=SESSION_TYPES)
    athlete = models.ForeignKey(Athlete,on_delete=models.CASCADE, null=True)
    file = models.ForeignKey(Vbo,on_delete=models.CASCADE, null=True)
    data = models.TextField(null=True)
    maxV = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    peak_50m_speed = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    peak_100m_speed = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    peak_150m_speed = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    peak_200m_speed = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    peak_300m_speed = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    peak_400m_speed = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    peak_500m_speed = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    peak_750m_speed = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    peak_1000m_speed = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    peak_1500m_speed = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    peak_2000m_speed = models.DecimalField(max_digits=5, decimal_places=2, null=True)

class AthleteSessionPeak(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    session_peak = models.ForeignKey(SessionPeaks, on_delete=models.CASCADE)
    date_completed = models.DateField()

    class Meta:
        unique_together = ('athlete', 'session_peak')
