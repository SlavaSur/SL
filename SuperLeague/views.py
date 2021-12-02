from django.shortcuts import render
from random import choice
from .models import *
# Create your views here.

def gs (request):
    club = Club.objects.order_by('-rating')
    return render (request,'SuperLeague/gs.html', {'club': club})

def tours (request):
    tour = Tour.objects.all()
    return render (request,'SuperLeague/tours.html', {'tour': tour})

def Turnament_table (request):
    turn = Table.objects.all()
    return render (request, 'SuperLeague/turnament_table.html', {'turn': turn})

def tour(*args,**kwargs):
    cl = [*args]
    while cl != []:
      home = choice(cl)
      cl.remove(home)
      return home

#Функция для проведения матчей
def game():
  goal_hom = 0
  goal_aw = 0
  shot = [i for i in range(1,7)]
  for _ in range (1,11):
    shot_home = random.choice(shot)
    if shot_home == 1:
      goal_hom += 1
  for _ in range (1,11):
    shot_away = random.choice(shot)
    if shot_away == 1:
      goal_aw += 1
  return goal_hom, goal_aw