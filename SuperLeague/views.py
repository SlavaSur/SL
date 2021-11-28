from django.shortcuts import render
from .models import Club
# Create your views here.
def gs (request):
    club = Club.objects.order_by('-rating')
    return render (request,'SuperLeague/gs.html', {'club': club})