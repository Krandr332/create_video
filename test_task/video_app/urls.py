from django.urls import path
from .views import video_view, video_create

urlpatterns = [
    path('', video_view, name='video_form'),
    path('create/', video_create, name='video_create'),
]
