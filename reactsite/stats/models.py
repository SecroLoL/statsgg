from djongo import models
from django import forms
from pymongo import MongoClient

client = MongoClient("mongodb+srv://<username>:<password>@cluster0.8b6cg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database('test')
records = db.champions

# Create your models here.
class Player(models.Model):
    # League id + username
    
    player_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    
class Champion(models.Model):
    
    champion_id = models.AutoField(primary_key=True)
    
class Test(models.Model):
    name = models.CharField(max_length=200)
    