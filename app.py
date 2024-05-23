import os
import spotipy
import spotipy.util as util
from dotenv import dotenv_values
from spotipy.oauth2 import SpotifyOAuth



# REDIRECT_URI = "https://mwendwatech.000webhostapp.com"
# token = util.prompt_for_user_token( username = "puppykiwi",
                                    # scope = SCOPE,
                                    # client_id= ID,
                                    # client_secret= SECRET,
                                    # redirect_uri= REDIRECT_URI)
# sp_oauth = SpotifyOAuth(client_id=ID,
                        # client_secret=SECRET,
                        # redirect_uri=REDIRECT_URI,
                        # scope=SCOPE)
# 
# token_info = sp_oauth.get_access_token()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=ID,
                                               client_secret=SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

# refresh_token = sp['refresh_token']

results = sp.current_user_saved_tracks()

if __name__ == "__main__":
    # print(sp['access_token'], "refresh token {}",refresh_token)
    # print(results)
    
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])
    print("** DONE **")
    