from PIL import Image
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


cover_art_path = 'cover_art/'
bmp_cover_art_path = 'cover_art/bmp/'

lz_uri = 'spotify:artist:3TVXtAsR1Inumwj472S9r4'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_top_tracks(lz_uri)

def download_cover_art(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(cover_art_path+filename, 'wb') as f:
            f.write(response.content)
    else:
        print("Error downloading cover art")

# Convert downloaded image to a 32x32 pixel bmp image
def convert_cover_art_to_32x32_bmp(filename):
    img = Image.open(cover_art_path+filename)
    img = img.resize((32, 32))
    img.save(bmp_cover_art_path + filename + '32x32.bmp')

for track in results['tracks'][:10]:
    track_name = track['name']
    artist = track['artists'][0]['name']
    track_name_for_filename = track_name.replace(' ', '_') + '-' + artist.replace(' ', '_') + '.jpg'
    cover_art_url = track['album']['images'][0]['url']
    print('track    : ' + track_name)
    print('artist   : ' + artist)
    print('cover art: ' + cover_art_url)

    download_cover_art(cover_art_url, track_name_for_filename)
    convert_cover_art_to_32x32_bmp(track_name_for_filename)
    print()

