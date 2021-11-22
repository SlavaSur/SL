from django.db import models

# Create your models here.
class Club (models.Model):
    club_name = models.CharField (max_length=50)
    coutry = models.CharField (max_length=3)
    rating = models.IntegerField ()

    # def __str__(self):
    #     return self.club_name
class Tour_one(models.Model):
    home = models.ForeignKey ('Club', on_delete=models.CASCADE,)
    goal_home = models.IntegerField()
    #away = models.ForeignKey ('Club', on_delete=models.CASCADE,)
    goal_away = models.IntegerField()
#class Tournament_table(Club):
    # position = models.AutoField(primary_key=True)
    # game = models.IntegerField(max_length=3)
    # goal_difference = models.IntegerField(max_length=3)
    # point = models.IntegerField(max_length=3)
