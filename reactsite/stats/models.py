from djongo import models
from django import forms

# To update these models to the database, py manage.py makemigrations/migrate
# The format for PostgreSQL "relations"/'models'/collections/columns is ex: stats_player, stats_champion. 
# So it takes react app name + _ + lower case name of class

# SQL syntax
# \d; to get all info of database
# SELECT * FROM <model_name>; get all from a specific model


# Create your models here.
class Player(models.Model):
    # League id + username
    
    player_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    
class Champion(models.Model):
    
    champion_id = models.AutoField(primary_key=True)
    
class Yo(models.Model):
    
    name = models.CharField(max_length=20)