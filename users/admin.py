from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.forms import TextInput, Textarea

class UserAdminConfig(UserAdmin):
    search_fields = ('emial', 'user_name', 'first_name',)
    ordering = ('-start_date',)
    list_display = ('emial', 'user_name', 'first_name',
                        'is_active', 'is_staff', 'is_coach', 'is_athlete')

    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_coach', 'is_athlete')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        User.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff', 'is_coach', 'is_athlete')}
         ),
    )
admin.site.register(User, UserAdminConfig)
