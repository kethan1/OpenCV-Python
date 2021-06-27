import cv2

video = cv2.VideoCapture("Videos/test_video.mp4")
wait_key_time = int((1 / int(video.get(cv2.CAP_PROP_FPS))) * 1000)

while video.isOpened():
    # ret is True or False, depending on if reading from
    # the camera was successful
    ret, frame = video.read()
    if ret:
        cv2.imshow("Camera", cv2.resize(frame, (960, 540)))
    else:
        # Makes the video loop
        video = cv2.VideoCapture("Videos/test_video.mp4")
    # Using just cv2.waitKey(1) plays the video too fast
    if cv2.waitKey(wait_key_time) == 27:
        print("Stopping Video")
        video.release()
        cv2.destroyAllWindows()
