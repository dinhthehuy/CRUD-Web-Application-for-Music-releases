from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('album/<album_id>', views.get_album, name='albums'),
    path('artist/<artist_id>', views.get_artist, name='artists'),
    path('search', views.search_album, name='search'),
    path('add/<album_id>/<album_name>/<artist_id>/<artist_name>/<release_date>/<num_songs>/<log_date>/', views.add_log, name='add'),
    path('delete/<artist_id>/<album_id>/', views.delete_log, name='delete'),
    path('tag/<album_tag>', views.get_albums_by_tag, name='tag')
]
