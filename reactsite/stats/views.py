from .models import Match
from .serializers import MatchSerializer
from rest_framework import generics, status
# Create your views here.

class MatchView(generics.ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    
    