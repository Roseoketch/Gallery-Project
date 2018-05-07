# # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Photos
import datetime as dt

# Create your views here.
def my_gallery(request):
    photos = Photos.objects.all()
    return render(request, 'index.html', {"photos":photos})

def single_photo(request, photo_id):
    photo = Photos.objects.get(id=photo_id)
    return render(request, 'photo.html', {'photo':photo})

def search_results(request):
    if 'photos' in request.GET and request.GET['photos']:
        search_term = request.GET.get('photos')
        searched_photo = Photos.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'all-pics/search.html', {"message":message, "photos":searched_photo})
    else:
        message = "You haven't searched for any photos."
        return render(request, 'all-pics/search.html', {"message":message})

def past_pics (request, past_date):
    #Convert date from the url string

    try:
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        raise Http404()
        assert False

    if date ==dt.date.today():
        return redirect(todays_pics)
    pics=Photo.days_pics(date)
    return render(request, 'all-pics/past_pics.html', {"date": date})
