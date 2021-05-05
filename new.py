import spotipy
from spotipy import util
from spotipy.oauth2 import SpotifyClientCredentials

def get_playlist_tracks(sp, username,playlist_id):
    results = sp.user_playlist_tracks(username,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

#Set up Spotify Connection
client_id = 'd5ec1915e2b3452f87cd1f224551a935'
f = open("secret.txt", "r")
client_secret = str(f.read())
username = '16r49f73ryoeuabwxqwgpimzs'
scope = 'user-library-read playlist-modify-public playlist-modify-private playlist-read-private'
redirect_uri='http://localhost:8888/callback'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)

playlist_id = input("Your playlist id: ")
trackslist = get_playlist_tracks(sp, username, playlist_id)
#results = sp.playlist(playlist_id=playlist_id)


for item in trackslist:
    songname = item['track']['name']
    songid = item['track']['id']
    mainartistname = item['track']['artists'][0]['name']
    mainartistid = item['track']['artists'][0]['id']
    print(songname, mainartistname, sep=' - ')