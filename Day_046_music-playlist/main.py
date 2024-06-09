import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI")


#=== Last.FM similart artist finder Code ====

artist = input("Pleast type the name of an artist to search for: ").replace(" ", "+")
# artist = "nightwish"

response = requests.get(f"https://www.last.fm/search?q={artist}")
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
sections = soup.find_all(name= "section")
# section = soup.select_one(selector="section h2 a").getText()
section = sections[1]
artist_first_result = section.find(class_ ="link-block-target").getText()
print(artist_first_result)
print("\n")
response = requests.get(f"https://www.last.fm/music/{artist_first_result}/+similar")
soup = BeautifulSoup(response.text, "html.parser")
similar_artists_list = soup.find_all(class_="similar-artists-item-name")
lastfm_similar_artists_list = [i.select_one(selector="h3 a").getText() for i in similar_artists_list]
# for i in similar_artists_list:
#     print(i.select_one(selector="h3 a").getText())

print(lastfm_similar_artists_list)

# references
# <a href="/music/quasimode" itemprop="url" class="link-block-target">quasimode</a>
# class ="grid-items-item-main-text" >
# class="similar-artists-item-name"


#=== Spotify Code ====

scope = "streaming"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=scope))

artist_uri_list = []
for a in lastfm_similar_artists_list:
    results = sp.search(q=f'artist: {a}', type='artist', limit=5)
    items = results['artists']['items']
    # print(items)
    if len(items) > 0:
        for artist in items:
            if a.lower() == artist['name'].lower():
                # print(artist['name'], artist["uri"])
                artist_uri_list.append(artist["uri"])

for a in artist_uri_list:
    artist_top_tracks = sp.artist_top_tracks(artist_id=a)
    for track in artist_top_tracks['tracks'][:1]:
        print('track    : ' + track['name'])
        print('audio    : ' + track['preview_url'])
        print('cover art: ' + track['album']['images'][0]['url'])
        print()

        sp.add_to_queue(track['uri'])

    # results = sp.current_user_saved_tracks()
    # for idx, item in enumerate(results['items']):
    #     track = item['track']
    #     print(idx, track['artists'][0]['name'], " – ", track['name'])
