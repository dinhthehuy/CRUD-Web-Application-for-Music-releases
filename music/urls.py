from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('album/<album_id>', views.get_album, name='albums'),
    path('artist/<artist_id>', views.get_artist, name='artists'),
    path('search', views.search_album, name='search'),
    path('add/<album_id>/<path:album_name>/<artist_id>/<path:artist_name>/', views.add_log, name='add'),
    path('delete/<log_id>/', views.delete_log, name='delete'),
    path('update/<album_id>/', views.update_album, name='update'),
    path('tag/<path:album_tag>', views.get_albums_by_tag, name='tag'),
    path('log', views.get_log_pagination, name='log'),
    path('log/year', views.get_log_by_year, name='log_by_year'),
    path('save-note', views.save_note, name='save_note'),
]
