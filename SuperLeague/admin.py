from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(Club)
class ClubAdmin (admin.ModelAdmin):
    list_display = ('id','club_name','coutry','rating')

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('home','goal_home','goal_away', 'away')

@admin.register(Table)
class TourAdmin(admin.ModelAdmin):
    list_display = ('club_name','played','gd', 'pts')