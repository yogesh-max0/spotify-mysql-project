from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import re

# Authenticate
sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id='1157318e14b442e387c9227947b82278',
        client_secret='9b2fd384e15547eea19450b73dbf4ba1'
    )
)

playlist_url = "https://open.spotify.com/playlist/0DM6a23TB90tZ6PaXYsiIP"
playlist_id = re.search(r'playlist/([a-zA-Z0-9]+)', playlist_url).group(1)

playlist = sp.playlist(playlist_id)
print("Playlist Name:", playlist["name"])

tracks = playlist["tracks"]["items"]

playlist_data = []
for item in tracks:
    track = item["track"]
    playlist_data.append({
        "Track Name": track["name"],
        "Artist": track["artists"][0]["name"],
        "Album": track["album"]["name"],
        "Popularity": track["popularity"],
        "Duration (min)": track["duration_ms"] / 60000
    })

df = pd.DataFrame(playlist_data)
print(df)
df.to_csv("spotify_playlist_data.csv", index=True)

# Plot Top 10 Popularity
top10 = df.sort_values(by="Popularity", ascending=False).head(10)
plt.figure(figsize=(10,5))
plt.bar(top10["Track Name"], top10["Popularity"], color='pink', edgecolor='grey')
plt.xticks(rotation=90)
plt.title(f"Top 10 Track Popularity - {playlist['name']}")
plt.ylabel("Popularity")
plt.tight_layout()
plt.show()
