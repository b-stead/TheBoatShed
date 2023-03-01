from django.shortcuts import render
from django.urls import reverse_lazy

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'SRC'))

def OnWater_home(request):
    return render(request, 'OnWater/Onwater.html')

def OnWater_vbo(request):
    return render(request, 'OnWater/vbo_load.html')    

