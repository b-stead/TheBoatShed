from django.shortcuts import render

# Create your views here.

def vbox_info(request):
    return render(request, 'vbox/vbox_info.html')