from django.conf.urls import url,include
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^new/',views.create_profile,name='new_profile'),
    url(r'^post/',views.new_post,name='post'),

]
