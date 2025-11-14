import mysql.connector
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import re

# Spotify API Auth
sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id='1157318e14b442e387c9227947b82278',
        client_secret='9b2fd384e15547eea19450b73dbf4ba1'
    )
)

# MySQL Database Config
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'spotify'
}

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# REAL playlist URL (YOURS)
playlist_url = 'https://open.spotify.com/playlist/0DM6a23TB90tZ6PaXYsiIP'

# Extract playlist ID
playlist_id = re.search(r'playlist/([a-zA-Z0-9]+)', playlist_url).group(1)

# Get playlist info
playlist = sp.playlist(playlist_id)
playlist_name = playlist['name']

tracks = playlist["tracks"]["items"]

# Insert each track
insert_query = """
INSERT INTO spotify_tracks
(playlist_name, track_name, artist, album, popularity, duration_minutes)
VALUES (%s, %s, %s, %s, %s, %s)
"""

for item in tracks:
    track = item["track"]

    data = (
        playlist_name,
        track["name"],
        track["artists"][0]["name"],
        track["album"]["name"],
        track["popularity"],
        track["duration_ms"] / 60000
    )

    cursor.execute(insert_query, data)

connection.commit()

print(f"\nInserted {len(tracks)} tracks from playlist '{playlist_name}' into MySQL.")

cursor.close()
connection.close()
