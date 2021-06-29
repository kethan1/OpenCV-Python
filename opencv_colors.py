import cv2

grayscale_image = cv2.imread("Images/image_with_colors.png", cv2.IMREAD_GRAYSCALE)
black_and_white_image = cv2.imread("Images/image_with_colors.png", cv2.COLOR_BGR2GRAY)
# img is a numpy array

cv2.imshow("Test Image", cv2.resize(grayscale_image, (550, 535)))
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imwrite("Images/grayscale_image.jpg", grayscale_image)
cv2.imwrite("Images/black_and_white_image.jpg", black_and_white_image)
