from django.db import models
from django import forms

# To update these models to the database, py manage.py makemigrations/migrate
# The format for PostgreSQL "relations"/'models'/collections/columns is ex: stats_player, stats_champion.
# So it takes react app name (stats) + _ + lower case name of class (player) (case ignored). Spaces are also ignored

# SQL syntax
# \d; to get all info of database
# SELECT * FROM <model_name>; get all from a specific model
# INSERT INTO <model_name>(<fields>) VALUES <values>. THE REASON WHY IT WILL SAY column "EBOMBERR" does not exist is because
# You have to use '' instead of ""
#

# Create your models here.


class Player(models.Model):
    # League id + username

    player_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class Champion(models.Model):

    champion_id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'Champion {str(self.champion_id)}'

# Anyway to create new table in pgAdmin then send it to the models.py?


class Match(models.Model):

    class Meta:
        verbose_name_plural = 'Matches'

    match_id = models.AutoField(primary_key=True)
    champion = models.IntegerField()
    championName = models.CharField(max_length=30)
    spell1 = models.IntegerField()
    spell2 = models.IntegerField()
    win = models.BooleanField()
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()
    totalDamageDealt = models.IntegerField()
    goldEarned = models.IntegerField()
    champLevel = models.IntegerField()
    totalMinionsKilled = models.IntegerField()
    item0 = models.IntegerField()
    item1 = models.IntegerField()

    def __str__(self):
        return f'{self.championName}, {self.champLevel}, {self.kills}, {self.deaths}, {self.assists}, {self.totalMinionsKilled}, {self.totalDamageDealt}'
