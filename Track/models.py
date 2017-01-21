from django.db import models
from Genre.models import Genres
class Tracks(models.Model):
    track_name = models.CharField(max_length=100, unique=True)
    track_genre = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now=True)
    track_rating= models.IntegerField(default=5)

    def __str__(self):
        return self.track_name
    def get_absolute_url(self):
        return "/music/details/%s/" %(self.id)