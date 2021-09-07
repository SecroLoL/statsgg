from .models import Match, Player
from .serializers import PlayerSerializer, MatchSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
import py_trading
import os
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.
# Make the views the standard CRUD (create, read, update, delete)


class Assets(View):

    def get(self, _request, filename):  # Handling when a HttpResponse is sent to user
        # The views.py in your React frontend needs a content_type argument in the HttpResponse.
        # Heroku needs to know where the static files are.

        # The "refused to execute script ... MIME type ('text/html')" problem stems from Django's default content_type setting for an HttpResponse, which is text/html.

        # This can be fixed by including a content_type='application/javascript' argument in the return statement of a new class-based view called Assets(View) inside views.py like so:
        path = os.path.join(os.path.dirname(__file__), 'static', filename)

        if os.path.isfile(path):
            with open(path, 'rb') as file:
                return HttpResponse(file.read(), content_type='application/javascript')
        else:
            return HttpResponseNotFound()


class PlayerView(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class MatchView(generics.ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
