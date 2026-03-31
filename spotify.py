import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def play_song_by_name(song_name):
	load_dotenv()
    results = sp.search(q=song_name, limit=1, type='track')
    
	scope="user-modify-playback-state"

	sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    if results['tracks']['items']:
        track_uri = results['tracks']['items'][0]['uri']
        track_name = results['tracks']['items'][0]['name']
        artist_name = results['tracks']['items'][0]['artists'][0]['name']
        
        print(f"Playing: {track_name} by {artist_name}")
        
        sp.start_playback(uris=[track_uri])
    else:
        print("Song not found.")

play_song_by_name(sys.argv[1])

