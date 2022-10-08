from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Account, Team
from .forms import LoginForm, SignUpForm, TeamForm


def home(request):
    if request.method == "GET":
        try:
            user = Account.objects.get(id=request.user.id)
            team = user.team

            print("00000000000000000000000000000000000")
            print(user)
            print("00000000000000000000000000000000000")
            print(team)
            print("00000000000000000000000000000000000")
            
            team_name = "None"
            if team:
                team_name = team.name
            return render(request, 'home.html' ,{"team": team_name})
        except:
            return redirect('login')

def signup(request):
    if request.method == "GET":
        form = SignUpForm()
        context = {"form": form}
        return render(request, "signup.html", context)

    elif request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)

            return redirect('team')

        else:
            return redirect('signup')
  
def login_account(request):
    if request.method == "GET":
        form = LoginForm()
        context = {"form": form}
        return render(request, "login.html", context)
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')

def logout_account(request):
    if request.method == "GET":
        logout(request)
        return redirect('login')

@login_required
def joinoradd_team(request):
    if request.method == "GET":
        user = Account.objects.get(id=request.user.id)
        if user.team:
            return redirect('home')
        else:
            form = TeamForm()
            context = {"form": form}
            return render(request, "team.html", context)

    elif request.method == "POST":
        form = TeamForm(request.POST)

        if form.is_valid():
            team_name = form.cleaned_data['name']

            team_exists = Team.objects.filter(name=team_name).exists()

            user = Account.objects.get(id=request.user.id)
 
            if team_exists:
                user.team = Team.objects.get(name=team_name)
            else:
                team_url = "http://meet.jit.si/" + team_name
                Team.objects.create(name=team_name, jitsi_url_path=team_url)
                team = Team.objects.get(name=team_name)
                user.team = team
                user.save()
        
        return redirect('home')

def exit_team(request):
    if request.method == "GET":
        user = Account.objects.get(id=request.user.id)
        if user.team is not "None":
            user.team = None
        
        user.save()
        return redirect('home')
