from rest_framework import serializers
from .models import Match, Player, Champion


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class ChampionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Champion
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match
        fields = '__all__'
