from datetime import datetime
from django.core.management.base import BaseCommand

from ...models import FootballTeam, Matches


def combinantorial(teams):
    index = 1
    pairs = []
    for team1 in teams:
        for team2 in teams[index:]:
            pairs.append((team1, team2))
            Matches.objects.create(first_team=team1, second_team=team2)
        index += 1
    return pairs


class Command(BaseCommand):
    help = 'Create matches of the day'
    """
    Can run this BaseCommand when execute this command (python manage.py create_matches_of_the_day)
    in the terminal make a setting in crontab which automatically executes it every day
    """
    def handle(self, *args, **options):
        now=datetime.now()
        matches_of_the_day = Matches.objects.filter(date_created=(datetime(now.year, now.month, now.day)))
        if matches_of_the_day.count() == 0:
            combinantorial(FootballTeam.objects.all())


