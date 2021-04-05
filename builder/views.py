from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from builder.forms import UserForm, UserProfileForm
from django.views import View
from builder.models import UserProfile, Team, FriendRequest, Pokemon, Move, Ability, Item, Nature

# Create your views here.

def home(request):
    #create team lists for home page display
    #popular teams order by views and new teams order by most recently added
    #Homepage shows a list of the most liked teams of all time, more button to see an extended list on another page


    visitor_cookie_handler(request)

    #find out html address!!

    team_database = Team.objects.all()
    popular_team_list = Team.objects.order_by('likes.count()')[:6]
    recent_team_list = Team.objects.all()[:6]
    context_dict = {'popularteamlist': popular_team_list, 'recentteamlist':recent_team_list, 'Team_database': team_database}

    response = render(request, 'home.html', context_dict)
    return response

def team_view(request, slug):
    team_view = get_object_or_404(Team, slug=slug)
    team_database = Team.objects.all()
    pokemon_database = Pokemon.objects.all()
    move_database = Move.objects.all()
    
    visitor_cookie_handler(request)
    
    return render(request, 'add_team.html', {'teamview' : team_view,
                                             'Team_database': team_database,
                                             "showpokemon": pokemon_database,
                                             "showmove": move_database
                                             })

def popular(request):
    #shown when more button clicked on  home page to the side of most popular teams

    popular_team_list = Team.objects.order_by('likes.count()')
    
    context_dict = {}
    context_dict['popularteamlist'] = popular_team_list

    visitor_cookie_handler(request)

    #find out html address!!

    response = render(request, 'builder/popular.html', context=context_dict)
    return response

def recent(request):
    #shown when more button clocked on the home page to the side of the most recent teams
    new_team_list = Team.objects.order_by('id')[:4]
    
    context_dict = {}
    context_dict['recentteamlist'] = new_team_list

    visitor_cookie_handler(request)

    #find out html address!!

    response = render(request, 'builder/recent.html', context=context_dict)
    return response

@login_required(login_url='/restricted/')
def Your_teams(request):

        #list  of public teams
        team_list = Team.objects.filter(userprofile = request.user)
        #list of private teams

        context_dict = {}
        context_dict['teams'] = team_list
        
        visitor_cookie_handler(request)
        
        response = render(request, 'builder/share.html', context = context_dict)
        return response
    

def share_priv_username(request, username_private_slug):

    #list of private teams
    user = UserProfile.objects.get(slug = username_private_slug)
    team_list = Team.objects.filter(userprofile = user)
    
    visitor_cookie_handler(request)
    
    context_dict = {}
    context_dict['teams'] = team_list
    response = render(request, 'builder/share.html', context = context_dict)
    return response


def share_username(request, username_slug):

    #list of public teams
    user = UserProfile.objects.get(slug = username_slug)
    team_list = Team.objects.filter(userprofile = user)
    
    visitor_cookie_handler(request)
    
    context_dict = {}
    context_dict['teams'] = team_list
    
    response = render(request, 'builder/share.html', context = context_dict)
    return response


def friends(request):

    #get list of friends

    friend_list = UserProfile.objects.values_list('friends', flat=True)
    #create dictionary of each friend and their teams
    friend_team_dict = {}
    for friend in friend_list:
        teams = Team.objects.filter(userprofile = friend)
        friend_team_dict[friend]=teams
        
    friend_requests = FriendRequest.object.filter(to_user=request.user)

    
    visitor_cookie_handler(request)

    context_dict = {}
    context_dict['friend_teams'] = friend_team_dict
    context_dict['friend_requests'] = friend_requests

    response = render(request, 'builder/friends.html', context = context_dict)
    return response


def viewfriend(request, friendname_slug):

    #get list of friendname_slug's teams
    
    user = UserProfile.objects.get(slug = friendname_slug)
    team_list = Team.objects.filter(user_profile=user)
    
    context_dict = {}
    context_dict['friend_teams'] = team_list
    
    response = render(request, '', context = context_dict)
    return response

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
    response = render(request, '', context = context_dict)
    return response

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
        return render(request, 'builder/login.html')

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
                  'builder/signup.html',
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

@login_required
def request_friend(request, username_slug):
    from_user = request.user
    to_user = UserProfile.objects.get(slug = username_slug)
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
