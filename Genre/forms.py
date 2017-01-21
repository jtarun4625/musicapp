from django import forms
from Genre.models import Genres

class AddGenreForm(forms.ModelForm):
    class Meta:
        model = Genres
        fields = [
            "genre_name",
        ]
