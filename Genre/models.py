from django.db import models

class Genres(models.Model):
    genre_name = models.CharField(max_length=25)
    def __str__(self):
        return self.genre_name