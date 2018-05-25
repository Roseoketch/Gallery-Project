from django.shortcuts import render, redirect
from django.http  import HttpResponse
import datetime as dt
from django.contrib.auth.decorators import login_required

# Create your views here.

def welcome(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')

@login_required(login_url='/accounts/login/')
def neighbor(request):
    date = dt.date.today()
    neighbor = Neighbor.objects.all()


    return render(request, 'groups.html', {"date": date,"neighbor":neighbor,})

# def new_neighbor(request):
#     current_user = request.user
#     form = NewNeihborForm()
#     if request.method == 'post':
#         form = NewHoodForm(request.POST, request.FILES)
#         if form.is_valid():
#             hood = form.save(commit=False)
#             hood.user = current_user
#         else:
#             if request.method == 'POST':
#                 form = myNewProfile(request.post,request.FILES)
#                 hood.user = current_user
#                 hood.save()
#                 return redirect('home')
#     return render(request, 'new-hood.html', {'form':form })
