from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from builder.forms import UserForm, UserProfileForm, Pokemon
from builder.models import Team, Pokemon, Move, Ability, Item, Nature
import json
from django.template.loader import render_to_string


# Create your views here.

def home(request):
    team_database = Team.objects.all()
    popular_team_list = Team.objects.order_by('-likes')[:6]
    recent_team_list = Team.objects.all()[::-1][:6]
    context_dict = {'popularteamlist': popular_team_list, 'recentteamlist':recent_team_list, 'Team_database': team_database}

    response = render(request, 'home.html', context_dict)
    return response

def team_view(request, slug):
    team_view = get_object_or_404(Team, slug=slug)
    team_database = Team.objects.all()
    pokemon_database = Pokemon.objects.all()
    move_database = Move.objects.all()
    return render(request, 'add_team.html', {'teamview' : team_view,
                                             'Team_database': team_database,
                                             "showpokemon": pokemon_database,
                                             "showmove": move_database
                                             })

def create_new_team(request):
    print("can't create new team")
    user_id = request.POST.get('user_id')
    print(user_id)
    teamname = request.POST.get('teamname')
    print(teamname)
    Team.objects.get_or_create(userprofile=user_id, teamname=teamname)

def popular(request):
    popular_team_list = Team.objects.order_by('-likes')
    return render(request, 'popular.html', context={'popularteams':popular_team_list})


def recent(request):
    recent_team_list = Team.objects.all()[::-1]
    return render(request, 'recent.html', context={'recentteams':recent_team_list})


@login_required(login_url='/restricted/')
def Your_Teams(request):
    user = request.user
    team_database = Team.objects.filter(userprofile=user)
    return render(request, 'your_teams.html', {'teamview':team_database})


@login_required(login_url='/restricted/')
def share_priv_username(request, username_private_slug):
    # list of private teams

    context_dict = {}


@login_required(login_url='/restricted/')
def share_username(request, username_slug):
    # list of public teams

    context_dict = {}


@login_required(login_url='/restricted/')
def friends(request):
    # get list of friends
    # get list of each friend's teams

    context_dict = {}
    return render(request, 'friends.html', context=context_dict)


@login_required(login_url='/restricted/')
def viewfriend(request, friendname_slug):
    # get list of friendname_slug's teams

    context_dict = {}

@login_required(login_url='/restricted/')
def builder(request):
    context_dict = {}
    context_dict['pokemon'] = Pokemon()
    pokemon_database = Pokemon.objects.all()
    move_database = Move.objects.all()
    nature_database = Nature.objects.all()
    ability_database = Ability.objects.all()
    item_database = Item.objects.all()
    return render(request, 'builder.html', {"showpokemon": pokemon_database,
                                            "showmove": move_database,
                                            "shownature": nature_database,
                                            "showability": ability_database,
                                            "showitem": item_database
                                            })


def buildteam(request, teamname_slug):
    context_dict = {}


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('builder:home'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'login.html')


def signup(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'signup.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('builder:home'))

def restricted(request):
    context_dict = {}
    return render(request, 'restricted.html', context=context_dict)


def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request,
                                               'last_visit',
                                               str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                        '%Y-%m-%d %H:%M:%S')

    # If it's been more than a day since the last visit...
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        # Update the last visit cookie now that we have updated the count
        request.session['last_visit'] = str(datetime.now())
    else:
        # Set the last visit cookie
        request.session['last_visit'] = last_visit_cookie

    # Update/set the visits cookie
    request.session['visits'] = visits
