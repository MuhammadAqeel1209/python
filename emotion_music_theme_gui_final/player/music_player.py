import os
import random
import pygame
from config import EMOTION_MUSIC_MAP

def play_music(emotion):
    pygame.mixer.init()
    folder = EMOTION_MUSIC_MAP.get(emotion)
    if folder and os.path.exists(folder):
        songs = [f for f in os.listdir(folder) if f.endswith('.mp3')]
        if songs:
            song_path = os.path.join(folder, random.choice(songs))
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()
        else:
            print(f"No songs found in {folder}")
    else:
        print(f"No folder found for emotion: {emotion}")
