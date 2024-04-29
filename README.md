# Music Info
[![en](https://img.shields.io/badge/lang-en-yellow.svg)](./README.md)

## Overview

Music Info is a simple CRUD web application used for looking up basic information about music albums. Also you can log what album you heard and when you heard it. The data is retrieved using Last.fm API and musicbrainz library. Sometimes the information (such as release date or no. tracks) from external APIs may be lacking or incorrect, these can be edited when logging. The cover art can also be changed.

This is a hobby project I created to learn web development and try out new tools such as Docker, Gunicorn, Nginx. The project contains both docker compose files for development and production. The latter uses Gunicorn as a WSGI production level server and Nginx to serve the static files (HTML, CSS, JS). 

### Screenshots 

### Roadmap
- [x] User's note can be saved in session and retrieved from database
- [x] Add pagination for logs 
- [ ] Template for artist, tag and year
- [ ] Filter for logs (by name, year,...)
- [ ] Improve saving user's note with AJAX 


## Getting Started
This guide helps you set up a copy of the project on your local machine.


### Prerequisites
* Python 3.11.5 (or higher)
* Django 5.0.2 (or higher)
* Docker (latest)

### Installation
1. Clone the repository to your local machine:
```
git clone https://github.com/dinhthehuy/Music-info
```
2. Navigate to project folder:
```
cd log-albums
``` 
4. Build docker compose image:
- For development:
```
docker compose -f docker-compose.yml build
```
- For production:
```
docker compose -f docker-compose.prod.yml build 
```
5. Run docker compose container:
- For development: 
```
docker compose -f docker-compose.yml up -d
```
localhost:5000/music/
- For production:
```
docker compose -f docker-compose.prod.yml
```
  localhost:1337/music/
