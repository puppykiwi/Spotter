import spotipy
from dotenv import dotenv_values
from spotipy.oauth2 import SpotifyOAuth

SCOPE = "user-read-playback-state,user-modify-playback-state,user-read-currently-playing, user-library-read"
ID = dotenv_values(".env")["ID"]
SECRET = dotenv_values(".env")["SECRET"]
URI = dotenv_values(".env")["REDIRECT_URI"]

sp_oauth = SpotifyOAuth(client_id=ID,
                        client_secret=SECRET,
                        redirect_uri=URI,
                        scope=SCOPE)

token_info = sp_oauth.get_access_token()

# Save in temp file
with open('.env', 'a') as f:
    f.write(f"\nSPOTIPY_ACCESS_TOKEN={token_info['access_token']}")
    f.write(f"\nSPOTIPY_REFRESH_TOKEN={token_info['refresh_token']}")

def get_spotify_client():
    sp = spotipy.Spotify(auth=token_info['access_token'])
    return sp

if __name__ == "__main__":
    sp = get_spotify_client()
    print(sp.current_playback())