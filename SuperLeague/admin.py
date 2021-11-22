from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(Club)
class ClubAdmin (admin.ModelAdmin):
    list_display = ('id','club_name','coutry','rating')

@admin.register(Tour_one)
class Tour_oneAdmin(admin.ModelAdmin):
    list_display = ('home','goal_home','goal_away')

@admin.register(Tournament_table)
class Tournament_tableAdmin(admin.ModelAdmin):
    list_display = ('position', 'game', 'goal_difference','point')

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'poz')