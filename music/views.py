import re
from datetime import datetime

import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from musicbrainzngs import musicbrainz as mbz

from .crud import insert_album, insert_logged_album, insert_artist, get_artist_by_id, insert_album_tag, \
    get_all_tags_by_album_id, get_all_albums_with_tag, get_album_by_id, get_all_albums_by_artist
from .models import Log

USER_AGENT = 'get_last_fm_data'
API_KEY = '101e8482407f74afceac4b4b38c19322'
url = 'https://ws.audioscrobbler.com/2.0/'
mbz.set_useragent('get_data', '0.1')


# Create your views here.
def index(request):
    logged_albums = Log.objects.order_by('-logged_date')
    log_count = Log.objects.count()
    return render(request, 'music/index.html', {'logged_albums': logged_albums, 'count': log_count})


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
    res = response['album']

    if res['mbid'] == '':
        return JsonResponse(response, safe=False)
    else:
        mbz_rg = mbz.search_release_groups(artistname=res['artist'], release=res['name'])['release-group-list'][0]
        mbz_release_date = mbz_rg.get('first-release-date')

        if mbz_release_date is None:
            mbz_release_date = '2000-01-01'
        elif re.fullmatch('\d{4}', mbz_release_date):
            mbz_release_date += '-01-01'
        elif re.fullmatch(r'\d{4}-\d{2}$', mbz_release_date):
            mbz_release_date += '-01'

        release_date = datetime.strptime(mbz_release_date, '%Y-%m-%d')
        artist_id = mbz_rg['artist-credit'][0]['artist']['id']
        num_songs = len(res.get('tracks')['track']) if res.get('tracks') else 0

        found_album = {
            'album_name': res['name'],
            'artist_name': res['artist'],
            'album_id': res['mbid'],
            'release_date': release_date,
            'artist_id': artist_id,
            'num_songs': num_songs,
        }
        image_url = res['image'][4]['#text']
    return render(request, 'music/search.html', context={'found_album': found_album, 'image_url': image_url})


def add_log(request, album_id, album_name, artist_id, artist_name):
    if request.method == 'POST':
        release_date = request.POST.get('release_date')
        log_date = request.POST.get('logged_date')
        num_songs = request.POST.get('num_songs')
        tags = mbz.search_release_groups(artistname=artist_name, release=album_name)['release-group-list'][0].get('tag-list')

        if get_artist_by_id(artist_id) is None:
            insert_artist(artist_id, artist_name)

        image_url = request.POST.get('image_url')

        if get_album_by_id(album_id) is None:
            insert_album(album_id, album_name, artist_id, release_date, num_songs, image_url)
            if tags is not None:
                for tag in tags:
                    insert_album_tag(album_id, tag['name'], tag['count'])
        insert_logged_album(album_id, artist_id, log_date)
    return redirect('index')


def delete_log(request, log_id):
    to_delete = Log.objects.get(id=log_id)
    to_delete.delete()
    return redirect('index')

def update_album(request, album_id):
    album = get_album_by_id(album_id)
    album.release_date = request.POST.get('release-date-edit')
    album.num_songs = request.POST.get('num-songs-edit')
    album.image_url = request.POST.get('cover-art-url-edit')
    album.save()
    return redirect('albums', album_id=album_id)