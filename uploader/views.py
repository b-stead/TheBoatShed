from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .owner import OwnerCreateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Vbo
from .forms import VboUploadForm


class VboCreateView(OwnerCreateView):
    model = Vbo
    form_class = VboUploadForm
    success_url = reverse_lazy('uploader:vbo_list')
    template_name = 'uploader/upload.html'

class VboListView(ListView):
    model = Vbo
    template_name = 'vbo_list.html'

"""
class VboCreateView(OwnerCreateView):
    model = Vbo
    form_class = VboUploadForm
    success_url = reverse_lazy('uploader:vbo_list')
    template_name = 'uploader/upload.html'

    #def form_valid(self, form):
     #   self.object = form.save(commit=False)
      #  self.object.owner = self.request.user
       # self.object.save()
        #return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Vbo.objects.all()
        return context

def vbo_process(request, pk):
    doc = get_object_or_404(Vbo, pk=pk)

    vbo_controller = VBoxController()
    df = vbo_controller.get_data(doc)
"""




    
