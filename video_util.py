import cv2

# In this file we are reading a video from disk and
# breaking it into frames using open cv

## the frames are saved as jpg images and passed to rest_service module

def video_to_frames(video_url):
	vidcap = cv2.VideoCapture(video_url)
	success,image = vidcap.read()
	count = 0
	frame_list = []
	while success:
		cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
		success,image = vidcap.read()
		frame_list.append("frame"+str(count)+".jpg")
		count += 1
	return frame_list
