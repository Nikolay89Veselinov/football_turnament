from django.contrib import admin

from .models import FootballTeam


@admin.register(FootballTeam)
class FootballTeam(admin.ModelAdmin):
    list_display = ('name',)
