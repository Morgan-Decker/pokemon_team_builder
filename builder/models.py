from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    friends = models.ManyToManyField('self')

    def __str__(self):
        return self.user.username
    
    
class FriendRequest(models.Model):
    from_user = models.ForeignKey(
        UserProfile, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User, related_name = 'to_user', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.from_user.user.username    

    
class Team(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    likes = models.ManyToManyField(UserProfile, related_name='team_like')

    pokedex1 = models.IntegerField()
    name1 = models.CharField(max_length=100)
    level1 = models.IntegerField()
    hp1 = models.IntegerField()
    attack1 = models.IntegerField()
    defence1 = models.IntegerField()
    sp_atk1 = models.IntegerField()
    sp_def1 = models.IntegerField()
    speed1 = models.IntegerField()
    type11 = models.CharField(max_length=10, default=None)
    type21 = models.CharField(max_length=10, default=None, blank=True, null=True)
    gigantamax_factor1 = models.IntegerField()

    pokedex2 = models.IntegerField()
    name2 = models.CharField(max_length=100)
    level2 = models.IntegerField()
    hp2 = models.IntegerField()
    attack2 = models.IntegerField()
    defence2 = models.IntegerField()
    sp_atk2 = models.IntegerField()
    sp_def2 = models.IntegerField()
    speed2 = models.IntegerField()
    type12 = models.CharField(max_length=10, default=None)
    type22 = models.CharField(max_length=10, default=None, blank=True, null=True)
    gigantamax_factor2 = models.IntegerField()

    pokedex3 = models.IntegerField()
    name3 = models.CharField(max_length=100)
    level3 = models.IntegerField()
    hp3 = models.IntegerField()
    attack3 = models.IntegerField()
    defence3 = models.IntegerField()
    sp_atk3 = models.IntegerField()
    sp_def3 = models.IntegerField()
    speed3 = models.IntegerField()
    type13 = models.CharField(max_length=10, default=None)
    type23 = models.CharField(max_length=10, default=None, blank=True, null=True)
    gigantamax_factor3 = models.IntegerField()

    pokedex4 = models.IntegerField()
    name4 = models.CharField(max_length=100)
    level4 = models.IntegerField()
    hp4 = models.IntegerField()
    attack4 = models.IntegerField()
    defence4 = models.IntegerField()
    sp_atk4 = models.IntegerField()
    sp_def4 = models.IntegerField()
    speed4 = models.IntegerField()
    type14 = models.CharField(max_length=10, default=None)
    type24 = models.CharField(max_length=10, default=None, blank=True, null=True)
    gigantamax_factor4 = models.IntegerField()

    pokedex5 = models.IntegerField()
    name5 = models.CharField(max_length=100)
    level5 = models.IntegerField()
    hp5 = models.IntegerField()
    attack5 = models.IntegerField()
    defence5 = models.IntegerField()
    sp_atk5 = models.IntegerField()
    sp_def5 = models.IntegerField()
    speed5 = models.IntegerField()
    type15 = models.CharField(max_length=10, default=None)
    type25 = models.CharField(max_length=10, default=None, blank=True, null=True)
    gigantamax_factor5 = models.IntegerField()

    pokedex6 = models.IntegerField()
    name6 = models.CharField(max_length=100)
    level6 = models.IntegerField()
    hp6 = models.IntegerField()
    attack6 = models.IntegerField()
    defence6 = models.IntegerField()
    sp_atk6 = models.IntegerField()
    sp_def6 = models.IntegerField()
    speed6 = models.IntegerField()
    type16 = models.CharField(max_length=10, default=None)
    type26 = models.CharField(max_length=10, default=None, blank=True, null=True)
    gigantamax_factor6 = models.IntegerField()

    def __str__(self):
        return self.name
    
    def number_of_likes(self):
        return self.likes.count()
