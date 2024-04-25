from .models import Dance, Artist, Performance
from django.forms import ModelForm, TextInput


class DanceForm(ModelForm):
    class Meta:
        model = Dance
        fields = ['dance_name', 'caption', 'native_name', 'genre', 'year', 'origin']

        widgets = {
            "dance_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Танго'
            }),
            "caption": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            "native_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя на языке оригинала'
            }),
            "year": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Год'
            }),
            "origin": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Страна происхождения'
            })
        }


class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'surname', 'country', 'gender']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Иван'
            }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Иванов'
            }),
            "country": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Страна'
            }),
            "gender": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пол'
            })
        }

class PerformanceForm(ModelForm):
    class Meta:
        model = Performance
        fields = ['title', 'date', 'country']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "date": TextInput(attrs={
                'class': 'form-control',
                'placeholder': '01-12-2002'
            }),
            "country": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Страна'
            })
        }
