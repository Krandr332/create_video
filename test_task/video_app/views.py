from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import VideoForm
from .models import VideoRequest
from .video_generator import create_video
from django.conf import settings
import os

def video_view(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            video_data = create_video(text)
            response = HttpResponse(video_data, content_type='video/mp4')
            response['Content-Disposition'] = f'attachment; filename="marquee_video.mp4"'
            return response
    else:
        form = VideoForm()

    return render(request, 'video_form.html', {'form': form})

def video_create(request):
    text = request.GET.get('text', '')
    if text:
        video_data = create_video(text)

        video_request = VideoRequest(text=text)
        video_request.save()

        response = HttpResponse(video_data, content_type='video/mp4')
        response['Content-Disposition'] = f'attachment; filename="marquee_video.mp4"'
        return response
    else:
        return HttpResponse("Пустой запрос", status=400)