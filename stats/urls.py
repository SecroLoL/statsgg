from django.urls import path
from .views import PlayerView

urlpatterns = [
    path('players', PlayerView.as_view()),
]


