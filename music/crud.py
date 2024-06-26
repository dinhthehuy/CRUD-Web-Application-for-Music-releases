from .models import Album, Artist, Log, AlbumTag


def get_album_by_id(album_id):
    return Album.objects.filter(mbid=album_id).first()


def get_artist_by_id(artist_id):
    return Artist.objects.filter(mbid=artist_id).first()


def get_log(album_id):
    return Log.objects.filter(album=album_id).first()

def get_log_by_release_year(year):
    return Log.objects.filter(album__release_date__year=f"{year}")

def get_log_by_release_name(name):
    return Log.objects.filter(album__name__icontains=name)

def get_log_by_artist_name(name):
    return Log.objects.filter(artist__name__istartswith=name)

def get_all_logged_albums():
    return Log.objects.all()


def get_all_tags_by_album_id(album_id):
    return AlbumTag.objects.filter(album=album_id).order_by('-count')


def get_all_albums_with_tag(tag):
    return AlbumTag.objects.filter(name=tag).order_by('-count')


def get_all_albums_by_artist(artist_id):
    return Album.objects.filter(artist=artist_id).order_by('release_date')


def insert_artist(artist_id, artist_name):
    new_artist = Artist(mbid=artist_id, name=artist_name)
    new_artist.save()
    return new_artist


def insert_album(album_id, album_name, artist_id, release_date, num_songs, image_url):
    artist = get_artist_by_id(artist_id)
    new_album = Album(mbid=album_id, name=album_name, artist=artist, release_date=release_date, num_songs=num_songs,
                      image_url=image_url)
    new_album.save()
    return new_album


def insert_logged_album(album_id, artist_id, logged_date):
    album = get_album_by_id(album_id)
    artist = get_artist_by_id(artist_id)
    new_logged_album = Log(album=album, artist=artist, logged_date=logged_date)
    new_logged_album.save()
    return new_logged_album


def insert_album_tag(album_id, tag, count):
    album = get_album_by_id(album_id)
    new_tag = AlbumTag(album=album, name=tag, count=count)
    new_tag.save()
    return new_tag
