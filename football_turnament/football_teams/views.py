from django.shortcuts import render, redirect

from .forms import FootballTeamForm


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
    
