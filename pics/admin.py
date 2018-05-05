# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Location, Photos, categories

# Register your models here.
admin.site.register(Location)
admin.site.register(categories)
admin.site.register(Photos)
