from django.urls import path
from django.views.generic import  ListView

from .views import create_football_team, filter_matches
from .models import FootballTeam, Matches

app_name = 'football_teams'
urlpatterns = [
    path('list_team/', ListView.as_view(model=FootballTeam), name="list_team",),
    path('create/', create_football_team, name="create",),
    path('filter_matches/', filter_matches, name="filter_matches",),
    path('matches/', ListView.as_view(model=Matches), name="matches",),
]
