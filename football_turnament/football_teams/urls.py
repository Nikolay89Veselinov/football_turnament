from django.urls import path

from .views import create_football_team


app_name = 'football_teams'
urlpatterns = [
    path('create/', create_football_team, name="create",),
]
