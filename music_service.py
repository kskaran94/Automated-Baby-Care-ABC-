import pygame
import time 

def play_music():
	pygame.mixer.music.load("music.mp3")
	pygame.mixer.music.play()

def stop_music():
	pygame.mixer.music.stop()


