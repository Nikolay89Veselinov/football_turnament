from django.db import models


class FootballTeam(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Football team'
        verbose_name_plural = 'Football teams'

    def __str__(self):
        return self.name


class Matches(models.Model):
    first_team = models.CharField(max_length=50)
    second_team = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)