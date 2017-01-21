from django import forms
from Track.models import Tracks

class AddtrackForm(forms.ModelForm):
    class Meta:
        model = Tracks
        fields = [
            "track_name",
            "track_genre",
            "track_rating"
        ]
