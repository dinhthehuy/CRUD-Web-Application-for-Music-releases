from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('album/<album_id>', views.get_album, name='albums'),
    path('artist/<artist_id>', views.get_artist, name='artists'),
    path('search', views.search_album, name='search'),
    path('add/<album_id>/<path:album_name>/<artist_id>/<path:artist_name>/', views.add_log, name='add'),
    path('delete/<log_id>/', views.delete_log, name='delete'),
    path('update/', views.update_album, name='update_album'),
    path('tag/<path:album_tag>', views.get_albums_by_tag, name='tag'),
]
