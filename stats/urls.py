from django.urls import path
from .views import PlayerView, MatchView

urlpatterns = [
    path('players', PlayerView.as_view()),
    path('matches', MatchView.as_view())
]
