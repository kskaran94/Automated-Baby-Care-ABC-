import pygame
import time

def play_music():
	pygame.mixer.music.load("music_service/music.mp3")
	print("the music is playing")
	pygame.mixer.music.play()

def stop_music():
	pygame.mixer.music.stop()
