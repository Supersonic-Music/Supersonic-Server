from flask import Flask, send_file, render_template, abort
import os
import urllib.parse

app = Flask(__name__)

# Define the directory where your music files are stored
MUSIC_DIR = "/home/deck/Music"

# Create a route to serve music files
@app.route('/music/<path:filename>')
def serve_music(filename):
    music_file = os.path.join(MUSIC_DIR, filename)

    if not os.path.isfile(music_file):
        return abort(404)  # File not found

    return send_file(music_file)

# Create a route to list artists and their albums
@app.route('/')
def index():
    artists = os.listdir(MUSIC_DIR)
    return render_template('index.html', artists=artists)

# Create a route to list albums for a specific artist
@app.route('/<artist>/')
def artist_albums(artist):
    artist_dir = os.path.join(MUSIC_DIR, artist)

    if not os.path.isdir(artist_dir):
        return abort(404)  # Artist directory not found

    # Sort the album directories numerically/lexicographically
    albums = sorted([item for item in os.listdir(artist_dir) if os.path.isdir(os.path.join(artist_dir, item))])
    return render_template('artist_albums.html', artist=artist, albums=albums)

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
    app.run(host='0.0.0.0', port=8083)