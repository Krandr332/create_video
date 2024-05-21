# Ваша модель models.py
from django.db import models

class VideoRequest(models.Model):
    text = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
