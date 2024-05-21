from django import forms

class VideoForm(forms.Form):
    text = forms.CharField(label='Text for Marquee', max_length=255)
