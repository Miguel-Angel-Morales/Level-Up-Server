from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=55, default="")
    maker = models.CharField(max_length=55, default="")
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    number_of_players = models.IntegerField(
        default=1,
        verbose_name="Number of Players",
        help_text="Enter the maximum number of players for this game."
    )

    SKILL_LEVEL_CHOICES = [
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
        (4, 'Expert'),
        (5, 'Master'),
    ]

    skill_level = models.IntegerField(
        default=1,
        choices=SKILL_LEVEL_CHOICES,
        verbose_name="Skill Level",
        help_text="Select the skill level required to play this game."
    )
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE)
    description = models.CharField(max_length=500, default="")
