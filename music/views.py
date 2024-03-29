import json
import re

import requests
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from .models import Log
from .crud import insert_album, insert_logged_album, insert_artist, get_artist_by_id, insert_album_tag, \
    get_all_tags_by_album_id, get_all_albums_with_tag, get_album_by_id, get_all_albums_by_artist
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
    album = get_album_by_id(album_id)
    tags = get_all_tags_by_album_id(album_id)
    return render(request, 'music/album.html', {'album': album, 'tags': tags})


def get_artist(request, artist_id):
    albums = get_all_albums_by_artist(artist_id)
    return render(request, 'music/artist.html', {'albums_by_artist': albums, 'artist': get_artist_by_id(artist_id)})


def get_albums_by_tag(request, album_tag):
    albums_by_tag = get_all_albums_with_tag(album_tag)

    albums = []
    for album in albums_by_tag:
        albums.append(album.album)
    return render(request, 'music/tag.html', {'tag': album_tag, 'albums': albums})


def search_album(request):
    response = requests.get(url, headers={'user-agent': USER_AGENT}, params={'api_key': API_KEY, 'format': 'json',
                                                                             'method': 'album.getInfo',
                                                                             'artist': request.GET.get('artist_name'),
                                                                             'album': request.GET.get('album_name'),
                                                                             'autocorrect': 1
                                                                             }).json()
    found_album = []
    res = response['album']

    if res['mbid'] == '':
        return JsonResponse(response, safe=False)
    else:
        # return JsonResponse(mbz.search_release_groups(reid=res['mbid'], strict=True), safe=False)
        mbz_rg = mbz.search_release_groups(reid=res['mbid'])['release-group-list'][0]
        release_date = mbz_rg.get('first-release-date')
        artist_id = mbz_rg['artist-credit'][0]['artist']['id']
        num_songs = len(res.get('tracks')['track']) if res.get('tracks') else 0

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

        tags = mbz.search_release_groups(reid=album_id)['release-group-list'][0].get('tag-list')

        if get_artist_by_id(artist_id) is None:
            insert_artist(artist_id, artist_name)

        image_url = request.POST.get('image_url')
        insert_album(album_id, album_name, artist_id, release_date, num_songs, image_url)
        insert_logged_album(album_id, artist_id, log_date)

        if tags is not None:
            for tag in tags:
                if "/" in tag['name']:
                    continue
                insert_album_tag(album_id, tag['name'], tag['count'])

    return redirect(reverse('index'))


def delete_log(request, artist_id, album_id):
    to_delete = Log.objects.get(artist_id=artist_id, album_id=album_id)
    to_delete.delete()
    return redirect(reverse('index'))
