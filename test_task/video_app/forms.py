from django import forms

class VideoForm(forms.Form):
    text = forms.CharField(label='text for the video', max_length=255)
