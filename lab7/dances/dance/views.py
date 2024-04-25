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
    template_name = 'dance/details.html'
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
        d = Dance.objects.all()
        if form1.is_valid() and form2.is_valid():
            dance_obj = Dance(dance_name=form2.cleaned_data.get("dance_name"),caption=form2.cleaned_data.get("caption"),
                              native_name=form2.cleaned_data.get("native_name"),
                              genre=form2.cleaned_data.get("genre"),year=int(form2.cleaned_data.get("year")),
                              origin=form2.cleaned_data.get("origin"))
            dance_obj.save()
            artist = Artist(name=form1.cleaned_data.get("name"), surname=form1.cleaned_data.get("surname"),
                            country=form1.cleaned_data.get("country"), gender=form1.cleaned_data.get("gender"),
                            dance_style=dance_obj)
            artist.save()

            '''artist_info = [form1.cleaned_data.get("name"), form1.cleaned_data.get("surname"),
                           form1.cleaned_data.get("country"), form1.cleaned_data.get("gender"), form1.cleaned_data.get("dance_style")]
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
        else:
            error = 'Неверно заполнены данные или такой пользователь уже есть' '''
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
