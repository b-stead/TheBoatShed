from dataclasses import fields
from django.contrib import admin
from .models import Vbo

class UploadAdmin(admin.ModelAdmin):
    model = Vbo
    fields = ['uploaded_at', 'session_date', 'crew', 'session']
    readonly_fields = ['uploaded_at']

admin.site.register(Vbo, UploadAdmin) 
