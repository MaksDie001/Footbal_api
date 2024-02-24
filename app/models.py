from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255)
    title = models.TextField()
    body = models.TextField()


class Matc(models.Model):
    date = models.DateTimeField(auto_created=True)
    name = models.CharField(max_length=255)
    body = models.TextField()
    first_team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='first_team_matches')
    second_team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='second_team_matches')
