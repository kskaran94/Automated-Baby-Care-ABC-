from playsound import playsound
from multiprocessing import Process
import threading

def start_music():
	p = Process(target=play_music)
	p.start()
	return p

def play_music():
	playsound('music.mp3')

def stop_music(p):
	p.terminate()