from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#from .forms import CustomUserCreationForm, CustomUserChangeForm
#from .models import CustomUser


"""
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    model = CustomUser

    list_display = ('username', 'email', 'is_active',
                    'is_staff', 'is_superuser', 'last_login','is_coach', 'is_athlete')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    #fields to be used for editing
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_coach', 'is_athlete',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login', 'date_joined')})
    )
    #fieldsets for creating users
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'is_coach', 'is_athlete')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)

"""
