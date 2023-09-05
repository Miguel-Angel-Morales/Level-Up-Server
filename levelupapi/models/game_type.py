from django.db import models

class GameType(models.Model):
    label = models.CharField(max_length=255, default="Default label")
    game_type = models.IntegerField(default=1)
    # other fields...



