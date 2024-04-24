from django.shortcuts import render
from django.http import HttpResponse

from .models import Dance, Artist, Performance
from .forms import DanceForm, ArtistForm, PerformanceForm
from django.views.generic import DetailView, UpdateView


# Create your views here.

def dance_home(request):
    a = Artist.objects.all()
    p = Performance.objects.all()
    d = Dance.objects.all()
    return render(request, 'dance/home.html', {'artist': a, 'performance': p, 'dance': d})

class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'dance/detail.html'
    context_object_name = 'artist'

class ArtistUpdateView(UpdateView):
    model = Artist
    template_name = 'dance/update.html'
    form_class = ArtistForm


def update(request):
    error = ''
    form = ArtistForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'dance/update.html', data)
def add(request):
    error = ''
    if request.method == 'POST':
        form1 = ArtistForm(request.POST)
        form2 = DanceForm(request.POST)
        a = Artist.objects.all()
        if form1.is_valid() and form2.is_valid():
            artist = Artist(name=form1.cleaned_data.get("name"), surname=form1.cleaned_data.get("surname"),
                            country=form1.cleaned_data.get("country"))
            artist_info = [form1.cleaned_data.get("name"), form1.cleaned_data.get("surname"),
                           form1.cleaned_data.get("country")]
            a_list = []
            for el in a:
                a_list.append([el.name, el.surname, el.country])
            if artist_info not in a_list:
                artist.save()
                error += "Пользователь добавлен."
            else:
                for el in a:
                    if artist_info[0] == el.name and artist_info[1] == el.surname and artist_info[2] == el.country:
                        artist = el
                error += "Пользователь уже существует."
            dance_form = Dance(dance_name=form2.cleaned_data.get("dance_name"),caption=form2.cleaned_data.get("caption"),
                              genre=form2.cleaned_data.get("genre"),)
            d = Dance.objects.all()
            p_list = Performance.objects.all()
        else:
            error = 'Неверно заполнены данные или такой пользователь уже есть'
    form1 = ArtistForm()
    form2 = DanceForm()
    data = {
        'form1': form1,
        'form2': form2,
        'error': error
    }
    return render(request, 'dance/add.html', data)
def dance_detail(request):
    context = {
        'title': 'detail'
    }
    return render(request, 'dance.index.html', context)


def dance_list(request):
    queryset = Dance.objects.all()
    if request.user.is_authenticated():
        context = {
            'queryset':queryset,
            'title': 'list authentication',
        }
    else:
        context = {
            'title': 'list authentication',
        }
    return render(request, 'index.html', context)
