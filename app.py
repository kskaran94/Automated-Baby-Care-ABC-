from image_process import image_process
from video.util import video_to_frames
from database.service import push

def initialize():
	cry_status = 0
	return cry_status


def main(video_url):
	count = 0
	cry_status = initialize()
	frame_list = video_to_frames(video_url)

	#video to frames
	for i in image_process(frame_list, cry_status):
		if i == 1:
			count +=1
			push([1,count,'crying'])
		else:
			count +=1
			push([1,count,'not_crying'])


#main()
