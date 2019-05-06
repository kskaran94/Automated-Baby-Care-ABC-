import json
import requests
from music_service.service import play_music, stop_music
from email_service.service import email_service
from config import subscription_key, face_api_url

## image_process processes an image and detect the emotion of the child based on
# threshold and returns a status.


def image_process(frame_list, cry_status):

    for i in range(0, len(frame_list), 100):
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

        response = requests.post(face_api_url, params=params, headers=headers,
                                data=data)

        sad_coeff = response.json()[0]['faceAttributes']['emotion']['sadness']
        if sad_coeff > 0.7: #pre-defined threshold
            if not cry_status:
                #play music
                #send notification
                music_process = play_music()
                email_service()
                cry_status = 1

        else:
            if cry_status:
                #stop music
                stop_music(music_process)
                cry_status = 0

        yield cry_status
        
    music_process.terminate()
