from django.contrib import admin

from music.models import Album, Artist, Log, AlbumTag

# Register your models here.
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Log)
admin.site.register(AlbumTag)
