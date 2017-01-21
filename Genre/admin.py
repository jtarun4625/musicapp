from django.contrib import admin
from Genre.models import Genres
class GenreAdmin(admin.ModelAdmin):
    class Meta:
        model = Genres

admin.site.register(Genres,GenreAdmin)
