from django.contrib import admin

from . import models

'''
admin.site.register(models.Dance)
admin.site.register(models.Artist)
admin.site.register(models.Performance)
'''


class DanceModelAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'timestamp', 'updated']
    class Meta:
        model = models.Dance


class ArtistModelAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Artist


class PerformanceModelAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Performance
