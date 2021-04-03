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
        UserProfile, related_name = 'from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User, related_name = 'to_user', on_delete=models.CASCADE)
