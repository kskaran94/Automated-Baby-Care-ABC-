import cv2
vidcap = cv2.VideoCapture('y2mate.com - baby_cryingmp4_1V5VPlmhdpc_360p.mp4')
success,image = vidcap.read()
count = 0
while success:
    cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1
