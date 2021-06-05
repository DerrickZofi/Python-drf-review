from django.db import models

# Create your models here.
class Music(models.Model):
    artist = models.CharField(max_length=100)
    song = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.artist