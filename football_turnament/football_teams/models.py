from django.db import models


class FootballTeam(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Football team'
        verbose_name_plural = 'Football teams'

    def __str__(self):
        return self.name