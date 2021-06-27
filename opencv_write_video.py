import cv2

cap = cv2.VideoCapture(0)

# *'XVID' for .avi
# *'mp4v' for .mp4
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter('Videos/video_write_test.mp4', fourcc, 20.0, (640, 480))

while True:
    retval, frame = cap.read()
    if retval:
        out.write(frame)
        cv2.imshow("Image", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    else:
        print("Could not get frame")
        break

cv2.destroyAllWindows()
cap.release()
out.release()
