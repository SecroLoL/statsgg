from django.db import models

# Create your models here.
class Player(models.Model):
    # League id + username
    
    player_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)