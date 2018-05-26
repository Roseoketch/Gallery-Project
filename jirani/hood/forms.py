from django  import forms
from .models import Neighbor,Business,MyUser,Post
from django.contrib.auth.models import User

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = MyUser
        exclude = ['user']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['editor','post_date']
