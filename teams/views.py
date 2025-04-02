from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Teams

# Create your views here.
def home(request):
    teams = Teams.objects.all()  # This gets all teams from the database
    return render(request, 'teams/home.html',{'teams': teams})

def add_teams(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        summary = request.POST.get('summary')
        image = request.FILES.get('image')
        
        Teams.objects.create(
            name=name,
            summary=summary,
            image=image
        )
        messages.success(request, 'Team added successfully!')
        return redirect('import')
    
    return render(request, 'teams/import.html')

def edit_team(request, team_id):
    team = get_object_or_404(Teams, id=team_id)
    
    if request.method == 'POST':
        team.name = request.POST.get('name')
        team.summary = request.POST.get('summary')
        
        if 'image' in request.FILES:
            team.image = request.FILES['image']
            
        team.save()
        messages.success(request, 'Team updated successfully!')
        return redirect('home')
    
    return render(request, 'teams/edit_team.html', {'team': team})