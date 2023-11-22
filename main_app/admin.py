from django.contrib import admin
from .models import Profile, Media, Posts, Feed, Messages
# Register your models here.
admin.site.register(Profile)
# admin.site.register(Media)
admin.site.register(Posts)
admin.site.register(Feed)
admin.site.register(Messages)