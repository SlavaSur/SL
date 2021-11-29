from django.urls import path
from . import views

urlpatterns = [
    path('', views.gs),
    path('tours/', views.tours),
]