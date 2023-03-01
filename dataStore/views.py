from django.shortcuts import render, redirect, get_object_or_404
from .SRC.vbox_controller import VBoxController
from uploader.models import Vbo
from .models import SessionPeaks
from .forms import SessionPeaksForm
from django.shortcuts import render
from django.http import HttpResponse
import os
import pandas as pd
import plotly.graph_objs as go

def vbo_process(request, pk):
    # assuming pk is the primary key of the uploaded file object
    vbo_instance = get_object_or_404(Vbo, pk=pk)
    session_peaks, created = SessionPeaks.objects.get_or_create(file=vbo_instance)
    filename = vbo_instance.file.path

    #send file to controller for processing
    controller = VBoxController(filename)
    df = controller.get_data()

    # calculate peak and average speeds for different distances
    peak_50m_speed = df['velocity'].rolling(window=50, min_periods=1).max().max()
    peak_100m_speed = df['velocity'].rolling(window=100, min_periods=1).max().max()
    avg_50m_speed = df['velocity'].rolling(window=50, min_periods=1).mean().max()
    avg_100m_speed = df['velocity'].rolling(window=100, min_periods=1).mean().max()

    # create plotly graph
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['SessionTime'], y=df['velocity'], mode='lines'))
    fig.update_layout(title='Speed vs Time')

    # create session peaks form
    if request.method == 'POST':
        form = SessionPeaksForm(request.user, request.POST, instance=session_peaks)
        if form.is_valid():
            session_peaks = form.save(commit=False)
            form.update_session_type(request.POST['session_type'])
            #session_peaks.file = filename
            #session_peaks.data = df.to_json() # convert dataframe to JSON and save it to the session peaks instance
            session_peaks.peak_50m_speed = peak_50m_speed
            session_peaks.peak_100m_speed = peak_100m_speed
            session_peaks.file = vbo_instance
            session_peaks.save()
            return redirect('dataStore/session_peaks_list')
        else:
            print(form.errors)


    else:
        form = SessionPeaksForm(request.user,instance=session_peaks)

    # render template with dataframe, plotly graph, and session peaks form
    context = {
        'pk': pk,
        'peak_50m_speed': peak_50m_speed,
        'peak_100m_speed': peak_100m_speed,
        'avg_50m_speed': avg_50m_speed,
        'avg_100m_speed': avg_100m_speed,
        'graph': fig.to_html(full_html=False, include_plotlyjs='cdn'),
        'form': form,
    }
    return render(request, 'dataStore/vbo_process.html', context)
