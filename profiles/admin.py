from django.contrib import admin

# Register your models here.
from . models import User, Athlete, Coach
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.forms import TextInput, Textarea

class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'user_name', 'first_name',)
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name',
                        'is_active', 'is_staff', 'is_coach', 'is_athlete', 'is_superuser')

    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_coach', 'is_athlete', 'is_superuser')}),
        ('Personal', {'fields': ('bio','profile_pic')}),
    )
    formfield_overrides = {
        User.bio: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff', 'is_coach', 'is_athlete')}
         ),
    )
admin.site.register(User, UserAdminConfig)
admin.site.register(Athlete)
admin.site.register(Coach)