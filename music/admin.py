from django.contrib import admin

from music.models import Album, Artist, LoggedAlbum, AlbumTag

# Register your models here.
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(LoggedAlbum)
admin.site.register(AlbumTag)
