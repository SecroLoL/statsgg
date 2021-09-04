from .models import Player
from .serializers import PlayerSerializer
from rest_framework import generics, status
# Create your views here.

class PlayerView(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    

    
    