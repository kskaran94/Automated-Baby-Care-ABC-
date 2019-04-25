from music_service import play_music, stop_music


def decision_service(payload, already_crying):
	sad_coeff = payload[0]['faceAttributes']['emotions']['sadness']
	if sad_coeff > 0.7: #pre-defined threshold
		if not already_crying:
			#play music
			#send notification
			play_music()
			email_service()
			already_crying = 1

	else:
		if already_crying:
			#stop music
			stop_music()
			already_crying = 0

	return already_crying


def initialize():
	pygame.init()
	already_crying = 0

	return already_crying



def main():
	already_crying = initialize()
	#video to frames
	payload = predict_service(image frame) #predict service
	already_crying = decision_service(payload, already_crying)