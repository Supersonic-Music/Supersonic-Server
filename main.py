#!/usr/bin/python

from flask import Flask, send_file, render_template, abort
from flask_cors import CORS
from info import ProgramData
from lightyear import generate_lightyear_stats
ProgramData = ProgramData()
from config import UserOptions
UserOptions = UserOptions()
import urllib.parse, os, jsonify

app = Flask(__name__)
CORS(app)

# Define the directory where your music files are stored
MUSIC_DIR = UserOptions.MUSIC_DIR
CAL_DIR = UserOptions.CAL_DIR

app.config['SECRET_KEY'] = "rubrub123"

@app.route('/Users/AuthenticateByName', methods=['POST'])
def authenticate_endpoint():
    data = request.get_json()
    username = data.get('Username')
    password = data.get('Pw')
    token = authenticate(app.config['SECRET_KEY'], username, password)
    if token is not None:
        return jsonify({'AccessToken': token}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

# Create a route to serve music files
@app.route('/music/<path:filename>')
def serve_music(filename):
    music_file = os.path.join(MUSIC_DIR, filename)

    if not os.path.isfile(music_file):
        return abort(404)  # File not found
    print("User listened to " + music_file)
    if music_file.rsplit('.', 1)[1] in UserOptions.MUSIC_FILETYPES:
        with open(UserOptions.LIGHTYEAR_PATH, "a") as song_log:
            song_log.write(filename + "\n")
    return send_file(music_file)

# Create a route to list artists and their albums
@app.route('/')
def index():
    artists = os.listdir(MUSIC_DIR)
    PROGRAM_NAME = ProgramData.PROGRAM_NAME
    return render_template(
        'index.html', artists=artists, 
        PROGRAM_NAME=PROGRAM_NAME, 
        number_of_artists=stats["number_of_artists"], 
        number_of_albums=stats["number_of_albums"], 
        number_of_songs=stats["number_of_songs"],
        lightyear_songs_listened_to=lightyear_stats[0][0]["songs_listened_to"],
        lightyear_artists_listened_to=lightyear_stats[0][0]["artists_listened_to"],
        lightyear_albums_listened_to=lightyear_stats[0][0]["albums_listened_to"],
        lightyear_artists=lightyear_stats[1]
    )

# Create a route to list albums for a specific artist
@app.route('/<artist>/')
def artist_albums(artist):
    artist_dir = os.path.join(MUSIC_DIR, artist)

    if not os.path.isdir(artist_dir):
        return abort(404)  # Artist directory not found

    # Sort the album directories numerically/lexicographically
    albums = sorted([item for item in os.listdir(artist_dir) if os.path.isdir(os.path.join(artist_dir, item))])
    return render_template('artist_albums.html', artist=artist, albums=albums)

@app.route('/lightyear/')
def lightyear():
    PROGRAM_NAME = ProgramData.PROGRAM_NAME
    print(lightyear_stats)
    return render_template('lightyear.html', PROGRAM_NAME=PROGRAM_NAME, songs_listened_to=lightyear_stats[0][0]['songs_listened_to'], albums_listened_to=lightyear_stats[0][0]['albums_listened_to'], artists_listened_to=lightyear_stats[0][0]['artists_listened_to'], artists=lightyear_stats[1])

# Create a route to list songs for a specific album
@app.route('/<artist>/<album>/')
def album_songs(artist, album):
    artist_dir = os.path.join(MUSIC_DIR, artist)
    album_dir = os.path.join(artist_dir, album)

    if not os.path.isdir(album_dir):
        return abort(404)  # Album directory not found

    # Sort the songs numerically/lexicographically
    songs = sorted(os.listdir(album_dir))
    return render_template('album.html', artist=artist, album=album, songs=songs)

if __name__ == '__main__':
    if UserOptions.SCAN_COLLECTION_ON_STARTUP == True:
        from scan_music import scan_music
        stats = scan_music(MUSIC_DIR, CAL_DIR)
        lightyear_stats = generate_lightyear_stats(UserOptions.LIGHTYEAR_PATH)
    from waitress import serve
    serve(app=app, host="0.0.0.0", port=6969)
