from django.shortcuts import render, redirect
from django.http  import HttpResponse
import datetime as dt
from django.contrib.auth.decorators import login_required
from .models import MyUser,Neighbor,Post,Business
from .forms import CreateProfileForm,PostForm
# Create your views here.

def welcome(request):
    current_user = request.user
    profile = MyUser.get_user()
    posts = Post.get_post()
    return render(request,'index.html',{"current_user":current_user,
                                        "profile":profile,
                                        "posts":posts})



def home(request):
    return render(request, 'home.html')

@login_required(login_url='/accounts/login/')
def neighbor(request):
    date = dt.date.today()
    neighbor = Neighbor.objects.all()


    return render(request, 'hood.html', {"date": date,"neighbor":neighbor,})

def new_neighbor(request):
    current_user = request.user
    form = NewNeihborForm()
    if request.method == 'post':
        form = NewNeighborForm(request.POST, request.FILES)
        if form.is_valid():
            neighbor = form.save(commit=False)
            neighbor.user = current_user
        else:
            if request.method == 'POST':
                form = myNewProfile(request.post,request.FILES)
                neighbor.user = current_user
                neighbor.save()
                return redirect('home')
    return render(request, 'new-hood.html', {'form':form })


@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = CreateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = current_user
            new.save()
            return redirect(view_profile)
    else:
        form = CreateProfileForm()
    return render(request,'profile.html',{"form":form})


@login_required(login_url='/accounts/login/')
def neighbor(request):
    current_user = request.user
    myuser = MyUser.get_user()
    posts = Post.get_post()
    count = 0
    jirani= Neighbor.get_neighbor()
    neighbor = get_object_or_404(Neighbor)
    for jirani in neighbor:
        for user in myuser:
            if user.neighbor.id == jirani.id:
                count += 1
    neighbor.occupants_count = count
    neighbor.save()
    return redirect('view_neighbor')


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    myuser = MyUser.get_user()
    for user in myuser:
        if user.user.id == current_user.id:
            if request.method == 'POST':
                post_form = PostForm(request.POST,request.FILES)
                if post_form.is_valid():
                    post = post_form.save(commit=False)
                    post.editor = user
                    post.save()
                    return redirect(index)
            else:
                post_form = PostForm()
            return render(request,'post.html',{"post_form":post_form})
