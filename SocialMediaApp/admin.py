from django.contrib import admin

# Register your models here.
from .models import Profile,Post,Like,Comment,Tag,FollowersCount,Follow,Messages

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Follow)
admin.site.register(FollowersCount)
admin.site.register(Messages)