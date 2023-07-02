from django.db import models
from django.contrib.auth import get_user_model
import uuid
User=get_user_model()

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    dob=models.DateField(null=True,blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    Gender=models.CharField(max_length=1,choices=GENDER_CHOICES,null=True,blank=True)
    Bio=models.TextField(blank=True)
    website=models.URLField(null=True,blank=True)
    Place=models.CharField(max_length=255,null=True,blank=True)
    Picture=models.ImageField(upload_to='media',null=True,blank=True,default='blankimage.jpg')

    def __str__(self) -> str:
        return self.user.username


class Post(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    caption=models.TextField()
    Publication_date=models.DateTimeField(auto_now_add=True)
    image_or_video=models.FileField(upload_to='media/postimages/')
    no_of_likes=models.IntegerField(default=0)

    def __str__(self):
        return self.caption
    
class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} likes {self.post.caption}'

class Comment(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    text=models.TextField()
    date_of_comment=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} commented on {self.post.caption}'


class Tag(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.name

class Follow(models.Model):
    follower=models.ForeignKey(User,related_name='following_relations',on_delete=models.CASCADE)
    following=models.ForeignKey(User,related_name='followers_relations',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.follower.username} follows {self.following.username}'

class FollowersCount(models.Model):
    
    follower = models.ForeignKey(User,on_delete=models.CASCADE,related_name='following_counts')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='followers_counts')
    def __str__(self):
        return f'{self.follower.username} follows {self.user.username}'
    
class Messages(models.Model):
    sender=models.ForeignKey(User,related_name='sent_messages',on_delete=models.CASCADE)
    receiptant=models.ForeignKey(User,related_name='received_messages',on_delete=models.CASCADE)
    content=models.TextField()
    time=models.DateTimeField(auto_now_add=True)