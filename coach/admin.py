from django.contrib import admin

# Register your models here.
from . models import User

@admin.register(User)
class user(admin.ModelAdmin):
    pass