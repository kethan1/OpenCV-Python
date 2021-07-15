import cv2

video = cv2.VideoCapture(0)

while video.isOpened():
    # ret is True or False, depending on if reading from
    # the camera was successful
    ret, frame = video.read()
    if ret:
        cv2.imshow("Camera", frame)
    if cv2.waitKey(1) == ord("q"):
        print("Stopping Video")
        video.release()
        cv2.destroyAllWindows()
