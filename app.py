import os
import spotipy
import spotipy.util as util
from dotenv import dotenv_values

ID = dotenv_values(".env")["ID"]
SECRET = dotenv_values(".env")["SECRET"]

# REDIRECT_URI = "https://mwendwatech.000webhostapp.com"
REDIRECT_URI = "http://localhost:8888/callback"
SCOPE = "user-library-read"

token = util.prompt_for_user_token( username = "puppykiwi",
                                    scope = SCOPE,
                                    client_id= ID,
                                    client_secret= SECRET,
                                    redirect_uri= REDIRECT_URI)



if __name__ == "__main__":
    print(ID, SECRET)