from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

class Team(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Pokemon(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    level = models.IntegerField()
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    sp_atk = models.IntegerField()
    sp_def = models.IntegerField()
    speed = models.IntegerField()

    type = ArrayField(models.CharField(max_length=10),
            size=2,)
    image = models.ImageField() #Need to choose upload to option
    gigantamax_factor = models.IntegerField()


class Move(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    contest = models.CharField(max_length=100)

    pp = models.IntegerField()
    power = models.IntegerField()
    accuracy = models.IntegerField()

class Ability(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Item(models.Model):
    pokemon = models.OneToOneField(Pokemon, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Nature(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
