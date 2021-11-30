import json
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import FootballTeamForm
from .models import Matches


def create_football_team(request):
    if request.method == 'POST':
        form = FootballTeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = FootballTeamForm()

    context = {
        'form': form,
    }
    return render(request, 'football_team.html', context)


def filter_matches(request):
    context = {}
    data = []
    if request.is_ajax():
        date = request.GET.get('match_date')
        if date != 'empty':
            date_dt3 = datetime.strptime(date, '%Y-%m-%d')
            matches_of_the_day = Matches.objects.filter(date_created=date_dt3.date()).all()
            for match in matches_of_the_day:
                data.append({
                    'first_team': match.first_team,
                    'second_team': match.second_team
                })
            json_content = json.dumps(data).encode('utf-8')
            return HttpResponse(json_content, 'applications/json; charset=utf-8')
    context.update({
        'matches': Matches.objects.all()
    })
    return render(request, 'filter_matches.html', context)
    
