from music_service import play_music, stop_music
import cv2
import json
import pygame
import requests

subscription_key = '1691e8e96bc64328aa7de93fd68b8c5e'
face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'


def decision_service(payload, already_crying):
	print(payload)
	sad_coeff = payload[0]['faceAttributes']['emotion']['sadness']
	if sad_coeff > 0.7: #pre-defined threshold
		if not already_crying:
			#play music
			#send notification
			play_music()
			#email_service()
			already_crying = 1

	else:
		if already_crying:
			#stop music
			#stop_music()
			already_crying = 0

	return already_crying


def initialize():
	pygame.init()
	already_crying = 0

	return already_crying

def video_to_frames(video_url):
	vidcap = cv2.VideoCapture(video_url)
	success,image = vidcap.read()
	count = 0
	frame_list = []
	while success:
		cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
		success,image = vidcap.read()
		frame_list.append("frame"+str(count)+".jpg")
		print('Read a new frame: ', success)
		count += 1
	return frame_list

def predict_service(frame_list):
	indices = []

	# Read file

	for i in range(0,len(frame_list),100):
		path_to_file = frame_list[i]
		with open(path_to_file, 'rb') as f:
			data = f.read()

		headers = dict()
		headers['Ocp-Apim-Subscription-Key'] = subscription_key
		headers['Content-Type'] = 'application/octet-stream'


		params = {
		    'returnFaceId': 'true',
		    'returnFaceLandmarks': 'false',
		    'returnFaceAttributes': 'emotion',
		}

		response = requests.post(face_api_url, params=params, headers=headers, data=data)
		return response.json()


def main():
	already_crying = initialize()
	video_url = 'y2mate.com - baby_cryingmp4_1V5VPlmhdpc_360p.mp4'
	frame_list = video_to_frames(video_url)
	#video to frames
	payload = predict_service(frame_list) #predict service
	already_crying = decision_service(payload, already_crying)
	print(already_crying)

main()
