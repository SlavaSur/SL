#from .views import game, tours
from django.db import models

# Create your models here.

class Club(models.Model):
    club_name = models.CharField (max_length=50)
    coutry = models.CharField (max_length=3)
    rating = models.IntegerField ()

    def __str__(self):
        return self.club_name

    class Meta:
        ordering = ["id"]

class Tour(models.Model):
    home = models.CharField (max_length=50) #SuperLeague.views.tours(Club.club_name),
    goal_home = models.IntegerField(default=0)
    goal_away = models.IntegerField(default=0)
    away = models.CharField(max_length=50)

class Table (models.Model):
    club_name = models.CharField(max_length=50)
    played = models.IntegerField (default=0)
    gd = models.IntegerField (default=0)
    pts = models.IntegerField (default=0)