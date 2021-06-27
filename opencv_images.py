import cv2

img = cv2.imread("Images/green_screen.jpg")
# img is a numpy array

cv2.imshow("Test Image", img)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imwrite("Images/test_write_image.jpg", img)
