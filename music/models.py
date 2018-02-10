from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=250)
    artist_title = models.CharField(max_length=220)
    genre = models.CharField(max_length=250)
    album_logo = models.CharField(max_length=240)
    def __str__(self):
        return self.artist_title +  '-' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=240)
    song_title = models.CharField(max_length=240)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

