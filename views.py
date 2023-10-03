from django.shortcuts import render, redirect
from .models import Song
from .forms import AddSongForm
# Create your views here.
def home(request):
    musics = Song.objects.all()
    return render(request, 'home.html', {'musics':musics})

def add(request):
    if request.method == 'POST':
        music_forms = AddSongForm(request.POST, request.FILES)
        if music_forms.is_valid():
            music_forms.save()
        else:
           return redirect('add') 
    return render(request, 'addPage.html')