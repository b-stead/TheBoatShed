from django.shortcuts import redirect, render
from django.views import View
from django.conf import settings

# Create your views here.

def OnWater_home(request):
    return render(request, 'OnWater/Onwater.html')

def OnWater_vbo(request):
    return render(request, 'OnWater/vbo_load.html')    
