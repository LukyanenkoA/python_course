from django.contrib import admin

from . import models


class DanceModelAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'native_name', 'genre']
    list_display_links = ['native_name', 'genre']
    list_filter = ['native_name', 'genre']
    search_fields = ['dance_name', 'native_name']

    class Meta:
        model = models.Dance


class ArtistModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'dance_style']
    search_fields = ['name', 'surname']
    list_display_links = ['name', 'surname']
    list_filter = ['name', 'surname']
    list_editable = ['dance_style']
    fields = ('name', 'surname', 'dance_style')

    class Meta:
        model = models.Artist


class PerformanceModelAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'date']
    search_fields = ['title', 'country']
    list_display_links = ['date']
    list_filter = ['date']

    class Meta:
        model = models.Performance


admin.site.register(models.Dance, DanceModelAdmin)
admin.site.register(models.Artist, ArtistModelAdmin)
admin.site.register(models.Performance, PerformanceModelAdmin)
