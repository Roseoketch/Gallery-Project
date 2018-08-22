from django.contrib import admin
from .models import Neighbor, Business, MyUser

# Register your models here.
admin.site.register(Neighbor)
admin.site.register(Business)
admin.site.register(MyUser)
