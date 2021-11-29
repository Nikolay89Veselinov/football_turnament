from django import forms
from django.db import models
from django.forms import fields

from .models import FootballTeam


class FootballTeamForm(forms.ModelForm):
    class Meta:
        model = FootballTeam
        fields = ('name',)