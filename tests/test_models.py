from django.test import TestCase

from music.models import Artist, Album, Log, AlbumTag

class TestArtist(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_artist = Artist.objects.create(mbid='12345', name='test_artist_name')
    def test_create_artist(self):
        self.assertEqual(self.test_artist.mbid, '12345')
        self.assertEqual(self.test_artist.name, 'test_artist_name')

class TestAlbum(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_album = Album.objects.create(mbid='23456', name='test_album_name',
                                              artist=Artist.objects.create(mbid='12345', name='test_artist_name'),
                                              release_date='2000-01-01', num_songs=8, image_url='url')
    def test_create_album(self):
        self.assertEqual(self.test_album.mbid, '23456')
        self.assertEqual(self.test_album.artist.mbid, '12345')

class TestLog(TestCase):
    @classmethod
    def setUpTestData(cls):
        artist = Artist.objects.create(mbid='12345', name='test_artist_name')
        cls.test_log = Log.objects.create(album=Album.objects.create(mbid='23456', name='test_album_name', artist=artist,
                                                                     release_date='2000-01-01', num_songs=8, image_url='url'),
                                          artist=artist,
                                          logged_date='2024-01-01')
    def test_create_log(self):
        self.assertEqual(self.test_log.album.mbid, '23456')
        self.assertEqual(self.test_log.artist.mbid, '12345')
        self.assertEqual(self.test_log.logged_date, '2024-01-01')

    def test_delete_log(self):
        self.test_log.delete()
        self.assertEqual(len(Log.objects.filter(logged_date='2024-01-01')), 0)

class TestAlbumTag(TestCase):
    @classmethod
    def setUpTestData(cls):
        artist = Artist.objects.create(mbid='12345', name='test_artist_name')
        album = Album.objects.create(mbid='23456', name='test_album_name', artist=artist, release_date='2000-01-01', num_songs=8, image_url='url')
        cls.test_album = album
        tags = [{'name': 'post-rock', 'count': 6}, {'name': 'shoegaze', 'count': 2}]
        for tag in tags:
            album_tag = AlbumTag(album_id='23456', name=tag['name'], count=tag['count'])
            album_tag.save()

    def test_create_album_tag(self):
        self.assertEqual(len(AlbumTag.objects.filter(album=self.test_album.mbid)), 2)


