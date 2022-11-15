from django.shortcuts import render
from .forms import CsvModelForm
from .models import Csv
import csv
# Create your views here.


def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)

            for i, row in enumerate(reader):
                if 1==0:
                    pass
                else:
                    date = row[1]
                    metric = row[2]
                    value = row[3]
    return render(request, 'uploader/uploader.html', {'form': form})
