import cv2

image = cv2.imread("../Images/image_with_colors.png")
image = cv2.circle(
    image,
    (20, 20),
    20,
    (255, 0, 0)
)


cv2.imshow('Test', image)
cv2.waitKey()
cv2.destroyAllWindows()
