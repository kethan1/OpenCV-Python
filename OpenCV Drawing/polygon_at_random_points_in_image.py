import cv2
import numpy as np
import random

image = cv2.imread("../Images/image_with_colors.png")
point1 = [
    random.randint(1, image.shape[1]),
    random.randint(1, image.shape[0]),
]
points = [np.array([
    point1,
    [
        random.randint(1, image.shape[1]),
        random.randint(1, image.shape[0])
    ],
    [
        random.randint(1, image.shape[1]),
        random.randint(1, image.shape[0]),
    ],
    point1
], dtype=np.int32).reshape((-1, 1, 2))]


image = cv2.polylines(
    image,
    points,
    True,
    (0, 0, 255),
    2
)


cv2.imshow('Test', image)
cv2.waitKey()
cv2.destroyAllWindows()
