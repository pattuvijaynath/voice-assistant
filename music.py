import time
import pytube
import vlc
from youtube_search import YoutubeSearch
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import time as pygame_time
import spotipy
import pygame
from spotipy.oauth2 import SpotifyClientCredentials


auth_manager = SpotifyClientCredentials(client_id='6805656204534066ad223bf44a3092b3', client_secret='31aed39616fe482fa9ebca3367da5852')
spotify = spotipy.Spotify(auth_manager=auth_manager)

def spotify_track_main_title(song):
    song_search = spotify.search(song, 1)
    song_title = song_search["tracks"]['items'][-1]['name']
    song_artist = song_search["tracks"]['items'][-1]['album']['artists'][0]['name']
    main_title = f'{song_title} by {song_artist}'
    return main_title


def play_song(song):
    search = YoutubeSearch(f'{song} lyrical', max_results=1).videos
    yt_url = f"https://youtube.com{search[0]['url_suffix']}"
    audio_url = pytube.YouTube(yt_url).streaming_data["adaptiveFormats"][-1]["url"]
    yt_song_title = search[0]['title']
    player = vlc.MediaPlayer(audio_url)
    player.play()
    print(f"started playing : {spotify_track_main_title(yt_song_title)}")
    print(audio_url)
    time.sleep(2)
    while player.is_playing():
        pygame_time.Clock().tick(10)






