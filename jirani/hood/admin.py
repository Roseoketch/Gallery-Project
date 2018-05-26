from django.contrib import admin
from .models import Neighbor, Business, MyUser, Post

# Register your models here.
admin.site.register(Neighbor)
admin.site.register(Business)
admin.site.register(MyUser)
admin.site.register(Post)
