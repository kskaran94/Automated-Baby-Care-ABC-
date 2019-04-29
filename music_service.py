import pygame
import time

def play_music():
	print("in music")
	pygame.mixer.music.load("music.mp3")
	print("in music2")
	pygame.mixer.music.play()

def stop_music():
	pygame.mixer.music.stop()
