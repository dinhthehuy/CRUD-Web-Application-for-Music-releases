# Generated by Django 5.0.3 on 2024-03-21 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('mbid', models.CharField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('mbid', models.CharField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('release_date', models.DateField(blank=True, null=True)),
                ('num_songs', models.IntegerField(blank=True, null=True)),
                ('image_url', models.CharField(blank=True, null=True)),
                ('artists', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logged_date', models.DateField(blank=True, null=True)),
                ('album', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.album')),
                ('artist', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.artist')),
            ],
        ),
        migrations.CreateModel(
            name='AlbumTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('count', models.IntegerField(blank=True, null=True)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.album')),
            ],
            options={
                'unique_together': {('album', 'name', 'count')},
            },
        ),
    ]
