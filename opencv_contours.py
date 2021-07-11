import cv2
import numpy as np

camera = cv2.VideoCapture(0)

number = 0
while True:
    ret, image = camera.read()
    if not ret:
        continue

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # Converts BGR image to HSV image for ease of use
    min_color = np.array([0, 0, 0])
    max_color = np.array([179, 239, 61])
    mask = cv2.inRange(hsv, min_color, max_color)  # Creates a mask of the image based on the min and max colors
    cv2.imshow("The Image", image)
    cv2.imshow("Mask", mask)

    contour_frame = mask.copy()
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour_frame = cv2.cvtColor(contour_frame, cv2.COLOR_GRAY2BGR)  # Need to convert back to color to draw contours
    # Sort the contours by area so that the number with the largest area is drawn.
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    cv2.drawContours(contour_frame, contours, 0, (0, 0, 255), 3)
    cv2.imshow("contours", contour_frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord("s"):
        print(333)
        cv2.imwrite(f"Images/thresholding_images/image{number}.jpg", image)
        number += 1

camera.release()
cv2.destroyAllWindows()
