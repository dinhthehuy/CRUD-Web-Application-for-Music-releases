import json
import re

import requests
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from .models import Album, Log
from .crud import insert_album, insert_logged_album, insert_artist, get_artist_by_id, get_log
from django.shortcuts import render, redirect
from musicbrainzngs import musicbrainz as mbz

USER_AGENT = 'get_last_fm_data'
API_KEY = '101e8482407f74afceac4b4b38c19322'
url = 'https://ws.audioscrobbler.com/2.0/'
mbz.set_useragent('get_data', '0.1')


# Create your views here.
def index(request):
    logged_albums = Log.objects.order_by('-logged_date')
    return render(request, 'music/index.html', {'logged_albums': logged_albums})


def get_album(request, album_id):
    response = requests.get(url, headers={'user-agent': USER_AGENT}, params={'api_key': API_KEY, 'format': 'json',
                                                                             'method': 'album.getInfo',
                                                                             'mbid': album_id}).json()
    return JsonResponse(response)


def get_artist(request, artist_id):
    response = requests.get(url, headers={'user-agent': USER_AGENT}, params={'api_key': API_KEY, 'format': 'json',
                                                                             'method': 'artist.getTopAlbums',
                                                                             'mbid': artist_id}).json()
    return JsonResponse(response)


def search_album(request):
    response = requests.get(url, headers={'user-agent': USER_AGENT}, params={'api_key': API_KEY, 'format': 'json',
                                                                             'method': 'album.getInfo',
                                                                             'artist': request.GET.get('artist_name'),
                                                                             'album': request.GET.get('album_name'),
                                                                             'autocorrect': 1
                                                                             }).json()
    found_album = []
    res = response['album']
    mbz_rg = mbz.search_release_groups(release=request.GET.get('album_name'),
                                       artistname=request.GET.get('artist_name'))['release-group-list']
    if res['mbid'] == '':
        return JsonResponse(response, safe=False)
    else:
        if res.get('tracks'):
            num_songs = len(res.get('tracks')['track'])
        else:
            num_songs = 0

        release_date = mbz_rg[0].get('first-release-date')
        artist_id = mbz_rg[0]['artist-credit'][0]['artist']['id']

        temp = {
            'album_name': res['name'],
            'artist_name': res['artist'],
            'album_id': res['mbid'],
            'logged_date': request.GET.get('logged_date'),
            'release_date': release_date,
            'artist_id': artist_id,
            'num_songs': num_songs,
        }
        image_url = res['image'][4]['#text']
        found_album.append(temp)
    return render(request, 'music/index.html', context={'found_album': found_album, 'image_url': image_url})


def add_log(request, album_id, album_name, artist_id, artist_name, release_date, num_songs, log_date):
    if request.method == 'POST':
        release_date = '2000-01-01' if not re.match(r'^\d{4}-\d{2}-\d{2}$', release_date) else release_date
        if get_artist_by_id(artist_id) is None:
            insert_artist(artist_id, artist_name)
        image_url = request.POST.get('image_url')
        insert_album(album_id, album_name, artist_id, release_date, num_songs, image_url)

        if not get_log(album_id):
            insert_logged_album(album_id, artist_id, log_date)
    return redirect(reverse('index'))


def delete_log(request, artist_id, album_id):
    to_delete = Log.objects.get(artist_id=artist_id, album_id=album_id)
    to_delete.delete()
    return redirect(reverse('index'))
