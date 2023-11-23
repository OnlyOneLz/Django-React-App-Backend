from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.IntegerField(default=0)
    email = models.CharField(max_length=100)
    # followers = models.IntegerField(default=0)
    # following = models.IntegerField(default=0)
    bio = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics/')

    def __str__(self):
        return f'{self.first_name} ({self.id})'
    

class Media(models.Model):
    title = models.CharField(max_length=30)
    document = models.FileField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f'


class Posts(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)

class Feed(models.Model):
    Posts = models.ForeignKey(Posts, on_delete=models.CASCADE)

class Messages(models.Model):
    sender_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='sent_messages'
    )
    
    receiver_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='received_messages'
    )
    
    message_content = models.CharField()

class Follows(models.Model):
    sender_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='my_profile'
    )
    
    receiver_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='following_profile'
    )


