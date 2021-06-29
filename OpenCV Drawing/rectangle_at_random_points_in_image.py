import cv2
import random

image = cv2.imread("../Images/image_with_colors.png")
image = cv2.rectangle(
    image,
    (
        random.randint(1, image.shape[1]),
        random.randint(1, image.shape[0]),
    ),
    (
        random.randint(1, image.shape[1]),
        random.randint(1, image.shape[0])
    ),
    (0, 0, 255)
)


cv2.imshow('Test', image)
cv2.waitKey()
cv2.destroyAllWindows()