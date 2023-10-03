from django.forms import widgets
from .models import Song
from django import forms

class AddSongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = [
            'music_name',
            'artiste',
            'time_length',
            'music_file',
            'cover_image'
        ]
