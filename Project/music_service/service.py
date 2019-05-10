import subprocess


def start_music():
	p = subprocess.Popen(['afplay', './music_service/music.mp3'])
	return p

def stop_music(p):
	p.terminate()