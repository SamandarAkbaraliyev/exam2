from django.db import models
from utils.models import BaseModel


class Country(BaseModel):
    flag = models.ImageField(upload_to='countries/')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Season(BaseModel):
    title = models.CharField(max_length=255, unique=True)  # example 2023/2024

    def __str__(self):
        return self.title


class League(BaseModel):
    title = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='leagues/')

    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='leagues', null=True, blank=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='leagues')

    def __str__(self):
        return self.title


class Stadium(BaseModel):
    title = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField(default=0)

    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='stadiums')

    def __str__(self):
        return self.title


class Club(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='clubs')

    stadium = models.OneToOneField(Stadium, on_delete=models.SET_NULL, null=True, related_name='club')
    leagues = models.ManyToManyField(League, related_name='clubs')

    def __str__(self):
        return self.title


class Player(BaseModel):
    class Position(models.TextChoices):
        GOALKEEPER = 'Goalkeeper'
        DEFENDER = 'Defender'
        MIDFIELDER = 'Midfielder'
        FORWARD = 'Forward'

    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='players/')
    birth_date = models.DateField(null=True)

    market_value = models.DecimalField(max_digits=10, decimal_places=2)
    position = models.CharField(max_length=64, choices=Position.choices, default=Position.GOALKEEPER)

    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, blank=True, related_name='players')
    contract_expires = models.DateField(null=True, default=None)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='players')

    def __str__(self):
        return self.full_name


class Match(BaseModel):
    host_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='host_matches')
    guest_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='guest_matches')

    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='matches')

    date_and_time = models.DateTimeField()
    is_finished = models.BooleanField(default=False)

    referee = models.CharField(max_length=255)
    attendance = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.host_club} vs {self.guest_club}"


class ClubMatchStatistics(BaseModel):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='club_match_statistic')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='club_match_statistic')
    xG = models.DecimalField(max_digits=4, decimal_places=2)

    ball_possession = models.IntegerField(default=0)
    goal_attempts = models.IntegerField(default=0)
    shots_on_goal = models.IntegerField(default=0)

    shots_off_goal = models.IntegerField(default=0)
    free_kicks = models.IntegerField(default=0)
    corner_kicks = models.IntegerField(default=0)

    offsides = models.IntegerField(default=0)
    throw_ins = models.IntegerField(default=0)
    saves = models.IntegerField(default=0)

    fouls = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)

    total_passes = models.IntegerField(default=0)
    tackles = models.IntegerField(default=0)
    attacks = models.IntegerField(default=0)

    dangerous_attacks = models.IntegerField(default=0)
    clearances = models.IntegerField(default=0)

    class Meta:
        unique_together = ['club', 'match']


class Goal(BaseModel):
    minute = models.IntegerField(default=0)

    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='goals')
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='goals')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='goals')


class Assist(BaseModel):
    goal = models.OneToOneField(Goal, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='assists')


class Substitution(BaseModel):
    player_in = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='substitutions_in')
    player_out = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='substitutions_out')

    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='substitutions')
    minute = models.IntegerField(default=0)

