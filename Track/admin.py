from django.contrib import admin
from Track.models import Tracks
# Register your models here.
class TrackAdmin(admin.ModelAdmin):
    list_display = ["track_name","timestamp","track_genre"]
    list_filter = ["track_name","track_genre"]
    search_fields = ["track_name","track_genre"]
    ordering = ["-timestamp"]
    class Meta:
        model = Tracks

admin.site.register(Tracks,TrackAdmin)