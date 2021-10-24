import lyricsgenius as lg
import pychromecast
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import tkinter as tk
import time
from tkinter import ttk
from tkinter import *


SPOTIPY_CLIENT_ID = "" # your spotify client id
SPOTIPY_CLIENT_SECRET = "" # your spotify secret
SPOTIPY_REDIRECT_URI = 'http://127.0.0.1/callback'
SCOPE = 'user-read-currently-playing'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=SCOPE))

def get_lyrics():
    now_playing = sp.current_user_playing_track()
    if now_playing is not None:
        artista = now_playing['item']['artists'][0]['name']
        name_song = now_playing['item']['name']
        length = now_playing['item']['duration_ms']
        progress = now_playing['progress_ms']
        print(artista, name_song, length, progress)
        info = ttk.Label(content, text = (artista  + ' - ' + name_song), font = ('Ubuntu', 20, 'bold'))
        info.grid(column = 0, row = 0, sticky = 'we')
        genius = lg.Genius('') '#insert your genius id here
        if (name_song.find('-') != -1):
            name_song1 = name_song[:(name_song.find('- ')-1)]
            try:
                letras2 = genius.search_song(name_song1, artista)
                letras3 = letras2.lyrics
                letras_box.delete('1.0', END)
                letras_box.insert('1.0', letras3)
            except Exception:
                letras_box.delete('1.0', END)
                letras_box.insert('1.0', 'INSTRUMENTAL')

        else:
            try:
                letras2 = genius.search_song(name_song, artista)
                letras3 = letras2.lyrics
                letras_box.delete('1.0', END)
                letras_box.insert('1.0', letras3)
            except Exception:
                letras_box.delete('1.0', END)
                letras_box.insert('1.0', 'INSTRUMENTAL')
        window.after(length - progress, get_lyrics)
    else:
        chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[""])#insert your chromecast or smart speaker name here
        [cc.device.friendly_name for cc in chromecasts]
        cast = chromecasts[0]
        cast.wait()
        print(cast.device)
        mc = cast.media_controller
        mc.block_until_active()
        print(mc.status)
        artist = mc.status.artist
        name_song = mc.status.title
        length = int(mc.status.duration)
        progress = int(mc.status.current_time)


        print(artist, name_song, length, progress)
        info = ttk.Label(content, text = (artist + ' - ' + name_song), font = ('Ubuntu', 20, 'bold'))
        info.grid(column = 0, row = 0, sticky = 'we')
        genius = lg.Genius('h2QlG7t_Xqz3U_719d0ak7ctJ_UXhejiQ1JhZPicysQwm_eC16nO0JSKWIx_ntXE')
        if (name_song.find('-') != -1):
            name_song1 = name_song[:(name_song.find('- ')-1)]
            try:
                letras2 = genius.search_song(name_song1, artist)
                letras3 = letras2.lyrics
                letras_box.delete('1.0', END)
                letras_box.insert('1.0', letras3)
            except Exception:
                letras_box.delete('1.0', END)
                letras_box.insert('1.0', 'INSTRUMENTAL')

        else:
            try:
                letras2 = genius.search_song(name_song, artist)
                letras3 = letras2.lyrics
                letras_box.delete('1.0', END)
                letras_box.insert('1.0', letras3)
            except Exception:
                letras_box.delete('1.0', END)
                letras_box.insert('1.0', 'INSTRUMENTAL')
        window.after(length*1000 - progress*1000, get_lyrics)

window = Tk()
window.title('Song lyrics')
ttk.Style().configure('TButton', font = ('Helvetica', 20, 'bold'))

content = tk.Frame(window, bg = 'gray1', borderwidth = 5, relief = 'ridge')
content.grid(column = 0, row = 1, sticky = (N, S, E, W))
scraper = ttk.Button(content, text = 'Lyrics', command = get_lyrics).grid(column = 0, row = 2, sticky = 'nw')
letras_box = results_box = tk.Text(content, font = ('Ubuntu', 20, 'bold'), width = 50, height = 40, fg = 'snow', bg = 'gray1')
letras_box.config(wrap = WORD)
letras_box.grid(column = 0, row = 1, sticky = 'nswe', columnspan = 2)
get_lyrics()
window.mainloop()
