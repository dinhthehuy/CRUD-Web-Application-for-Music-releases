# Music Info
[![en](https://img.shields.io/badge/lang-en-yellow.svg)](./README.md)

## Overview

Music Info is a simple CRUD web application used for looking up basic information about music albums. Additionally, you can log what you've heard and when you heard it. The data is retrieved using the Last.fm API and the Musicbrainz library. Sometimes, the information (such as release date or number of tracks) from external APIs may be lacking or incorrect; these can be edited when logging. The cover art can also be changed.

This is a hobby project I created to learn web development and try out new tools such as Docker, Gunicorn, and Nginx. The project contains both Docker Compose files for development and production. The latter uses Gunicorn as a WSGI production-level server and Nginx to serve the static files (HTML, CSS, JS).

### Screenshots 

### To do
- [x] User's note can be saved in session and retrieved from database
- [x] Add pagination for logs 
- [ ] Template for artist, tag and year
- [ ] Filter for logs (by name, year,...)
- [ ] Improve saving user's note with AJAX
- [ ] Deploy to vercel
- [ ] New feature: Recommendation


## Getting Started
This guide helps you set up a copy of the project on your local machine.


### Prerequisites
* Python 3.11.5 (or higher)
* Docker (latest)
* Pycharm (Optional)

### Installation
1. Clone the repository to your local machine:
```console
foo@bar:~$ git clone https://github.com/dinhthehuy/Music-info
```
2. Navigate to project folder:
```console
foo@bar:~$ cd log-albums
```
### Development
1. Build docker compose image:
```console
foo@bar:~$ docker compose -f docker-compose.yml build
```
2. Run docker compose container
```console
foo@bar:~$ docker compose -f docker-compose.yml up -d
```
Test it out at [http://localhost:5000/music/](http://localhost:5000/music/)

### Production
1. Build docker compose image
```console
foo@bar:~$ docker compose -f docker-compose.prod.yml build 
```
2. Run docker compose container
```console
foo@bar:~$ docker compose -f docker-compose.prod.yml up -d
```
Test it out at [http://localhost:1337/music/](http://localhost:1337/music/)
