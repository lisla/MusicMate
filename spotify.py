import bs4
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# ---- Get info from Spotify ----
# Find recent songs relating to band name
def search_new_songs(band_name):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

    results = sp.search(q='weezer', limit=20)
    for idx, track in enumerate(results['tracks']['items']):
        print(idx, track['name'])
    return
