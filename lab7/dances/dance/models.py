from django.db import models


class Dance(models.Model):
    dance_name = models.CharField(max_length=100)
    caption = models.TextField()
    native_name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    origin = models.CharField(max_length=100)

    def __unicode__(self):
        return self.dance_name

    def __str__(self):
        return ' '.join([
            self.dance_name,
            self.caption,
            self.native_name,
            self.genre,
            str(self.year),
            self.origin,
        ])

    class Meta:
        verbose_name = 'Dance'
        verbose_name_plural = 'Dances'
        db_table = 'Dance'
        ordering = ["dance_name"]


class Artist(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    dance_style = models.ForeignKey(Dance, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name + ' ' + self.surname

    def __str__(self):
        return ' '.join([
            str(self.name),
            str(self.surname),
            str(self.country),
            str(self.gender),
        ])

    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'
        db_table = 'Artist'
        ordering = ["name", "surname"]


class Performance(models.Model):
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    dance_style = models.ForeignKey(Dance, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return ' '.join([
            str(self.title),
            str(self.date),
            str(self.country),
        ])

    class Meta:
        verbose_name = 'Performance'
        verbose_name_plural = 'Performances'
        db_table = 'Performance'
        ordering = ["title"]
