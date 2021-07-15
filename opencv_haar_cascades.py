import cv2
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if not ret:
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # # perform face detection using the appropriate haar cascade
    faceRects = face_cascade.detectMultiScale(
        gray, scaleFactor=1.05, minNeighbors=3, minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (fX, fY, fW, fH) in faceRects:
        frame = cv2.rectangle(
            frame, (fX, fY), (fX + fW, fY + fH),
            (0, 255, 0), 2
        )

    cv2.imshow('Output', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
