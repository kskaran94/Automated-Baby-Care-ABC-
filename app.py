from image_process import image_process
from video_util import video_to_frames
from database.service import push

def initialize():
	cry_status = 0

	return cry_status


def main():
	count = 0
	cry_status = initialize()
	video_url = 'video0.mp4'
	frame_list = video_to_frames(video_url)

	#video to frames
	for i in image_process(frame_list, cry_status):
		if i == 1:
			count +=1
			push([1,count,'crying'])
		else:
			count +=1
			push([1,count,'not_crying'])


main()
