from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(Club)
class ClubAdmin (admin.ModelAdmin):
    list_display = ('id','club_name','coutry','rating')

# @admin.register(Tournament_table)
# class Tournament_tableAdmin(admin.ModelAdmin):
#     list_display = ('position', 'club_name', 'game', 'goal_difference','point')
@admin.register(Tour_one)
class Tour_1Admin(admin.ModelAdmin):
    list_display = ('home','goal_home','goal_away')