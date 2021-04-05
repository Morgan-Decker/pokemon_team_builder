from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from django.views import View
from builder.forms import UserForm, UserProfileForm
from builder.models import Team, Pokemon, Move, Ability, Item, Nature, UserProfile, FriendRequest


# Create your views here.

def home(request):
    team_database = Team.objects.all()
    popular_team_list = Team.objects.order_by('-likes')[:6]
    recent_team_list = Team.objects.all()[::-1][:6]
    context_dict = {'popularteamlist': popular_team_list, 'recentteamlist': recent_team_list,
                    'Team_database': team_database}

    response = render(request, 'home.html', context_dict)
    return response


def team_view(request, slug):
    team_view = get_object_or_404(Team, slug=slug)
    team_database = Team.objects.all()
    pokemon_database = Pokemon.objects.all()
    move_database = Move.objects.all()
    return render(request, 'add_team.html', {'teamview': team_view,
                                             'Team_database': team_database,
                                             "showpokemon": pokemon_database,
                                             "showmove": move_database
                                             })


class LikeTeamView(View):
    @login_required
    def get(self, request):
        team_id = request.GET['team_id']
        try:
            team = Team.objects.get(id=int(team_id))
        except Team.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)
        team.likes = team.likes + 1
        team.save()
        return HttpResponse(team.likes)


def popular(request):
    popular_team_list = Team.objects.order_by('-likes')
    return render(request, 'popular.html', context={'popularteams': popular_team_list})


def recent(request):
    recent_team_list = Team.objects.all()[::-1]
    return render(request, 'recent.html', context={'recentteams': recent_team_list})


@login_required(login_url='/restricted/')
def Your_Teams(request):
    user = request.user
    team_database = Team.objects.filter(userprofile=user)[::-1]
    return render(request, 'your_teams.html', {'teamview': team_database})


@login_required(login_url='/restricted/')
def share_priv_username(request, username_private_slug):
    # list of private teams

    context_dict = {}


@login_required(login_url='/restricted/')
def share_username(request, username_slug):
    # list of public teams

    context_dict = {}


def friends(request):
    # get list of friends

    friend_list = UserProfile.objects.values_list('friends', flat=True)
    # create dictionary of each friend and their teams
    friend_team_dict = {}
    for friend in friend_list:
        teams = Team.objects.filter(userprofile=friend)
        friend_team_dict[friend] = teams

    friend_requests = FriendRequest.objects.filter(to_user=request.user)

    visitor_cookie_handler(request)

    context_dict = {}
    context_dict['friend_teams'] = friend_team_dict
    context_dict['friend_requests'] = friend_requests

    response = render(request, 'friends.html', context=context_dict)
    return response


def viewfriend(request, friendname_slug):
    # get list of friendname_slug's teams

    user = UserProfile.objects.get(slug=friendname_slug)
    team_list = Team.objects.filter(user_profile=user)

    context_dict = {}
    context_dict['friend_teams'] = team_list

    response = render(request, '', context=context_dict)
    return response


@login_required
def request_friend(request, username_slug):
    from_user = request.user
    to_user = UserProfile.objects.get(slug=username_slug)
    friendrequest, created = FriendRequest.objects.get_or_create(
        from_user=from_user, to_user=to_user)
    if created:
        return HttpResponse('friend request sent')
    else:
        return HttpResponse('friend request was already sent')


@login_required
def accept_friend(request, requestID):
    friend_request = FriendRequest.object.get(id=requestID)
    to_user = friend_request.to_user
    from_user = friend_request.from_user
    if to_user == request.user:
        to_user.friends.add(from_user)
        from_user.friends.add(to_user)
        friend_request.delete()
        return HttpResponse('friend request accepted')
    else:
        return HttpResponse('friend request not accepted')


def LikeView(request, pk):
    team = get_object_or_404(Team, id=request.POST.get('team_id'))
    team.likes.add(request.user)
    return HttpResponseRedirect(reverse('team', args=[str.pk]))


@login_required(login_url='/restricted/')
def builder(request):
    context_dict = {}
    context_dict['pokemon'] = Pokemon()
    pokemon_database = Pokemon.objects.all()
    move_database = Move.objects.all()
    nature_database = Nature.objects.all()
    ability_database = Ability.objects.all()
    item_database = Item.objects.all()

    if request.method == 'POST':
        if request.POST.get('user_id') and request.POST.get('teamname'):

            def g(x):
                return request.POST.get(x)

            def authenticate_teamname(teamname):
                allteams = Team.objects.values_list('teamname', flat=True)
                j = 0
                while teamname in allteams:
                    j += 1
                    newteamname = teamname + str(j)
                    if newteamname not in allteams:
                        teamname = newteamname
                return teamname

            userprofile = g('user_id')
            teamname = g('teamname')

            pokedex1, name1, ability1, nature1, gmax1, item1 = g('pokedex1'), g('name1'), g('ability1'), g(
                'nature1'), g('gmax1'), g('item1')
            move1_1, move2_1, move3_1, move4_1, = g('move1_1'), g('move2_1'), g('move3_1'), g('move4_1')
            movetype1_1, movetype2_1, movetype3_1, movetype4_1 = g('movetype1_1'), g('movetype2_1'), g(
                'movetype3_1'), g('movetype4_1')
            level1, hp1, atk1, def1, sp_atk1, sp_def1, spd1 = g('level1'), g('hp1'), g('atk1'), g('def1'), g(
                'sp_atk1'), g('sp_def1'), g('spd1')
            hpEV1, atkEV1, defEV1, sp_atkEV1, sp_defEV1, spdEV1 = g('hpEV1'), g('atkEV1'), g('defEV1'), g(
                'sp_atkEV1'), g('sp_defEV1'), g('spdEV1')
            hpIV1, atkIV1, defIV1, sp_atkIV1, sp_defIV1, spdIV1 = g('hpIV1'), g('atkIV1'), g('defIV1'), g(
                'sp_atkIV1'), g('sp_defIV1'), g('spdIV1')
            type1_1, type2_1 = g('type1_1'), g('type2_1')
            pokedex2, name2, ability2, nature2, gmax2, item2 = g('pokedex2'), g('name2'), g('ability2'), g(
                'nature2'), g('gmax2'), g('item2')
            move1_2, move2_2, move3_2, move4_2, = g('move1_2'), g('move2_2'), g('move3_2'), g('move4_2')
            movetype1_2, movetype2_2, movetype3_2, movetype4_2 = g('movetype1_2'), g('movetype2_2'), g(
                'movetype3_2'), g('movetype4_2')
            level2, hp2, atk2, def2, sp_atk2, sp_def2, spd2 = g('level2'), g('hp2'), g('atk2'), g('def2'), g(
                'sp_atk2'), g('sp_def2'), g('spd2')
            hpEV2, atkEV2, defEV2, sp_atkEV2, sp_defEV2, spdEV2 = g('hpEV2'), g('atkEV2'), g('defEV2'), g(
                'sp_atkEV2'), g('sp_defEV2'), g('spdEV2')
            hpIV2, atkIV2, defIV2, sp_atkIV2, sp_defIV2, spdIV2 = g('hpIV2'), g('atkIV2'), g('defIV2'), g(
                'sp_atkIV2'), g('sp_defIV2'), g('spdIV2')
            type1_2, type2_2 = g('type1_2'), g('type2_2')
            pokedex3, name3, ability3, nature3, gmax3, item3 = g('pokedex3'), g('name3'), g('ability3'), g(
                'nature3'), g('gmax3'), g('item3')
            move1_3, move2_3, move3_3, move4_3, = g('move1_3'), g('move2_3'), g('move3_3'), g('move4_3')
            movetype1_3, movetype2_3, movetype3_3, movetype4_3 = g('movetype1_3'), g('movetype2_3'), g(
                'movetype3_3'), g('movetype4_3')
            level3, hp3, atk3, def3, sp_atk3, sp_def3, spd3 = g('level3'), g('hp3'), g('atk3'), g('def3'), g(
                'sp_atk3'), g('sp_def3'), g('spd3')
            hpEV3, atkEV3, defEV3, sp_atkEV3, sp_defEV3, spdEV3 = g('hpEV3'), g('atkEV3'), g('defEV3'), g(
                'sp_atkEV3'), g('sp_defEV3'), g('spdEV3')
            hpIV3, atkIV3, defIV3, sp_atkIV3, sp_defIV3, spdIV3 = g('hpIV3'), g('atkIV3'), g('defIV3'), g(
                'sp_atkIV3'), g('sp_defIV3'), g('spdIV3')
            type1_3, type2_3 = g('type1_3'), g('type2_3')
            pokedex4, name4, ability4, nature4, gmax4, item4 = g('pokedex4'), g('name4'), g('ability4'), g(
                'nature4'), g('gmax4'), g('item4')
            move1_4, move2_4, move3_4, move4_4, = g('move1_4'), g('move2_4'), g('move3_4'), g('move4_4')
            movetype1_4, movetype2_4, movetype3_4, movetype4_4 = g('movetype1_4'), g('movetype2_4'), g(
                'movetype3_4'), g('movetype4_4')
            level4, hp4, atk4, def4, sp_atk4, sp_def4, spd4 = g('level4'), g('hp4'), g('atk4'), g('def4'), g(
                'sp_atk4'), g('sp_def4'), g('spd4')
            hpEV4, atkEV4, defEV4, sp_atkEV4, sp_defEV4, spdEV4 = g('hpEV4'), g('atkEV4'), g('defEV4'), g(
                'sp_atkEV4'), g('sp_defEV4'), g('spdEV4')
            hpIV4, atkIV4, defIV4, sp_atkIV4, sp_defIV4, spdIV4 = g('hpIV4'), g('atkIV4'), g('defIV4'), g(
                'sp_atkIV4'), g('sp_defIV4'), g('spdIV4')
            type1_4, type2_4 = g('type1_4'), g('type2_4')
            pokedex5, name5, ability5, nature5, gmax5, item5 = g('pokedex5'), g('name5'), g('ability5'), g(
                'nature5'), g('gmax5'), g('item5')
            move1_5, move2_5, move3_5, move4_5, = g('move1_5'), g('move2_5'), g('move3_5'), g('move4_5')
            movetype1_5, movetype2_5, movetype3_5, movetype4_5 = g('movetype1_5'), g('movetype2_5'), g(
                'movetype3_5'), g('movetype4_5')
            level5, hp5, atk5, def5, sp_atk5, sp_def5, spd5 = g('level5'), g('hp5'), g('atk5'), g('def5'), g(
                'sp_atk5'), g('sp_def5'), g('spd5')
            hpEV5, atkEV5, defEV5, sp_atkEV5, sp_defEV5, spdEV5 = g('hpEV5'), g('atkEV5'), g('defEV5'), g(
                'sp_atkEV5'), g('sp_defEV5'), g('spdEV5')
            hpIV5, atkIV5, defIV5, sp_atkIV5, sp_defIV5, spdIV5 = g('hpIV5'), g('atkIV5'), g('defIV5'), g(
                'sp_atkIV5'), g('sp_defIV5'), g('spdIV5')
            type1_5, type2_5 = g('type1_5'), g('type2_5')
            pokedex6, name6, ability6, nature6, gmax6, item6 = g('pokedex6'), g('name6'), g('ability6'), g(
                'nature6'), g('gmax6'), g('item6')
            move1_6, move2_6, move3_6, move4_6, = g('move1_6'), g('move2_6'), g('move3_6'), g('move4_6')
            movetype1_6, movetype2_6, movetype3_6, movetype4_6 = g('movetype1_6'), g('movetype2_6'), g(
                'movetype3_6'), g('movetype4_6')
            level6, hp6, atk6, def6, sp_atk6, sp_def6, spd6 = g('level6'), g('hp6'), g('atk6'), g('def6'), g(
                'sp_atk6'), g('sp_def6'), g('spd6')
            hpEV6, atkEV6, defEV6, sp_atkEV6, sp_defEV6, spdEV6 = g('hpEV6'), g('atkEV6'), g('defEV6'), g(
                'sp_atkEV6'), g('sp_defEV6'), g('spdEV6')
            hpIV6, atkIV6, defIV6, sp_atkIV6, sp_defIV6, spdIV6 = g('hpIV6'), g('atkIV6'), g('defIV6'), g(
                'sp_atkIV6'), g('sp_defIV6'), g('spdIV6')
            type1_6, type2_6 = g('type1_6'), g('type2_6')
            d, created = Team.objects.get_or_create(teamname=authenticate_teamname(teamname), userprofile=userprofile,
                                                    likes=0,
                                                    pokedex1=pokedex1, name1=name1, ability1=ability1, nature1=nature1,
                                                    gmax1=gmax1,
                                                    item1=item1, move1_1=move1_1, move2_1=move2_1, move3_1=move3_1,
                                                    move4_1=move4_1,
                                                    movetype1_1=movetype1_1, movetype2_1=movetype2_1,
                                                    movetype3_1=movetype3_1, movetype4_1=movetype4_1,
                                                    level1=level1, hp1=hp1, atk1=atk1, def1=def1, sp_atk1=sp_atk1,
                                                    sp_def1=sp_def1, spd1=spd1,
                                                    hpEV1=hpEV1, atkEV1=atkEV1, defEV1=defEV1, sp_atkEV1=sp_atkEV1,
                                                    sp_defEV1=sp_defEV1, spdEV1=spdEV1,
                                                    hpIV1=hpIV1, atkIV1=atkIV1, defIV1=defIV1, sp_atkIV1=sp_atkIV1,
                                                    sp_defIV1=sp_defIV1, spdIV1=spdIV1,
                                                    type1_1=type1_1, type2_1=type2_1,
                                                    pokedex2=pokedex2, name2=name2, ability2=ability2, nature2=nature2,
                                                    gmax2=gmax2,
                                                    item2=item2, move1_2=move1_2, move2_2=move2_2, move3_2=move3_2,
                                                    move4_2=move4_2,
                                                    movetype1_2=movetype1_2, movetype2_2=movetype2_2,
                                                    movetype3_2=movetype3_2, movetype4_2=movetype4_2,
                                                    level2=level2, hp2=hp2, atk2=atk2, def2=def2, sp_atk2=sp_atk2,
                                                    sp_def2=sp_def2, spd2=spd2,
                                                    hpEV2=hpEV2, atkEV2=atkEV2, defEV2=defEV2, sp_atkEV2=sp_atkEV2,
                                                    sp_defEV2=sp_defEV2, spdEV2=spdEV2,
                                                    hpIV2=hpIV2, atkIV2=atkIV2, defIV2=defIV2, sp_atkIV2=sp_atkIV2,
                                                    sp_defIV2=sp_defIV2, spdIV2=spdIV2,
                                                    type1_2=type1_2, type2_2=type2_2,
                                                    pokedex3=pokedex3, name3=name3, ability3=ability3, nature3=nature3,
                                                    gmax3=gmax3,
                                                    item3=item3, move1_3=move1_3, move2_3=move2_3, move3_3=move3_3,
                                                    move4_3=move4_3,
                                                    movetype1_3=movetype1_3, movetype2_3=movetype2_3,
                                                    movetype3_3=movetype3_3, movetype4_3=movetype4_3,
                                                    level3=level3, hp3=hp3, atk3=atk3, def3=def3, sp_atk3=sp_atk3,
                                                    sp_def3=sp_def3, spd3=spd3,
                                                    hpEV3=hpEV3, atkEV3=atkEV3, defEV3=defEV3, sp_atkEV3=sp_atkEV3,
                                                    sp_defEV3=sp_defEV3, spdEV3=spdEV3,
                                                    hpIV3=hpIV3, atkIV3=atkIV3, defIV3=defIV3, sp_atkIV3=sp_atkIV3,
                                                    sp_defIV3=sp_defIV3, spdIV3=spdIV3,
                                                    type1_3=type1_3, type2_3=type2_3,
                                                    pokedex4=pokedex4, name4=name4, ability4=ability4, nature4=nature4,
                                                    gmax4=gmax4,
                                                    item4=item4, move1_4=move1_4, move2_4=move2_4, move3_4=move3_4,
                                                    move4_4=move4_4,
                                                    movetype1_4=movetype1_4, movetype2_4=movetype2_4,
                                                    movetype3_4=movetype3_4, movetype4_4=movetype4_4,
                                                    level4=level4, hp4=hp4, atk4=atk4, def4=def4, sp_atk4=sp_atk4,
                                                    sp_def4=sp_def4, spd4=spd4,
                                                    hpEV4=hpEV4, atkEV4=atkEV4, defEV4=defEV4, sp_atkEV4=sp_atkEV4,
                                                    sp_defEV4=sp_defEV4, spdEV4=spdEV4,
                                                    hpIV4=hpIV4, atkIV4=atkIV4, defIV4=defIV4, sp_atkIV4=sp_atkIV4,
                                                    sp_defIV4=sp_defIV4, spdIV4=spdIV4,
                                                    type1_4=type1_4, type2_4=type2_4,
                                                    pokedex5=pokedex5, name5=name5, ability5=ability5, nature5=nature5,
                                                    gmax5=gmax5,
                                                    item5=item5, move1_5=move1_5, move2_5=move2_5, move3_5=move3_5,
                                                    move4_5=move4_5,
                                                    movetype1_5=movetype1_5, movetype2_5=movetype2_5,
                                                    movetype3_5=movetype3_5, movetype4_5=movetype4_5,
                                                    level5=level5, hp5=hp5, atk5=atk5, def5=def5, sp_atk5=sp_atk5,
                                                    sp_def5=sp_def5, spd5=spd5,
                                                    hpEV5=hpEV5, atkEV5=atkEV5, defEV5=defEV5, sp_atkEV5=sp_atkEV5,
                                                    sp_defEV5=sp_defEV5, spdEV5=spdEV5,
                                                    hpIV5=hpIV5, atkIV5=atkIV5, defIV5=defIV5, sp_atkIV5=sp_atkIV5,
                                                    sp_defIV5=sp_defIV5, spdIV5=spdIV5,
                                                    type1_5=type1_5, type2_5=type2_5,
                                                    pokedex6=pokedex6, name6=name6, ability6=ability6, nature6=nature6,
                                                    gmax6=gmax6,
                                                    item6=item6, move1_6=move1_6, move2_6=move2_6, move3_6=move3_6,
                                                    move4_6=move4_6,
                                                    movetype1_6=movetype1_6, movetype2_6=movetype2_6,
                                                    movetype3_6=movetype3_6, movetype4_6=movetype4_6,
                                                    level6=level6, hp6=hp6, atk6=atk6, def6=def6, sp_atk6=sp_atk6,
                                                    sp_def6=sp_def6, spd6=spd6,
                                                    hpEV6=hpEV6, atkEV6=atkEV6, defEV6=defEV6, sp_atkEV6=sp_atkEV6,
                                                    sp_defEV6=sp_defEV6, spdEV6=spdEV6,
                                                    hpIV6=hpIV6, atkIV6=atkIV6, defIV6=defIV6, sp_atkIV6=sp_atkIV6,
                                                    sp_defIV6=sp_defIV6, spdIV6=spdIV6,
                                                    type1_6=type1_6, type2_6=type2_6
                                                    )
            print("- Data: {0}, Created: {1}".format(str(d), str(created)))
            messages.success(request, 'Team Saved Successfully...!')

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
