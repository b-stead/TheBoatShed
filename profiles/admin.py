from django.contrib import admin

# Register your models here.
from . models import User, Athlete
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

class ProfileInline(admin.StackedInline):
    model = Athlete
    can_delete = False
    verbose_name_plural = 'Athlete'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_coach', 'is_athlete')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {
            'fields': ('is_athlete', 'is_coach')
        }),
    )
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.register(User, CustomUserAdmin)
