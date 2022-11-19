from django.contrib import admin
from .models import CoachDemo, AthleteDemo, TeamDemo

# Register your models here.
myModels = [CoachDemo, AthleteDemo, TeamDemo]
admin.site.register(myModels)