from django.db import models

# Create your models here.
class Club (models.Model):
    club_name = models.CharField (max_length=50)
    coutry = models.CharField (max_length=3)
    rating = models.IntegerField ()

    def __str__(self):
        return self.club_name

    class Meta:
        ordering = ["id"]

class Tour(models.Model):
    home = models.CharField (max_length=50)
    goal_home = models.IntegerField()
    goal_away = models.IntegerField()
    away = models.CharField(max_length=50)

class Table (models.Model):
    club_name = models.CharField(max_length=50)
    played = models.IntegerField (default=0)
    gd = models.IntegerField (default=0)
    pts = models.IntegerField (default=0)