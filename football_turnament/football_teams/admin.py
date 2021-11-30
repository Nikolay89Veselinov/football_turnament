from django.contrib import admin

from .models import FootballTeam, Matches


@admin.register(FootballTeam)
class FootballTeam(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Matches)
class MatchesTeam(admin.ModelAdmin):
    list_display = ('first_team', 'second_team', 'date_created')
