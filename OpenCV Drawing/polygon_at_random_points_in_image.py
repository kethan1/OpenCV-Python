import cv2
import numpy as np
import random

image = cv2.imread("../Images/image_with_colors.png")
point1 = [
    random.randint(1, image.shape[1]),
    random.randint(1, image.shape[0]),
]
number_of_random_points = random.randint(2, 5)  # Random number of points
points = [
    np.array([
        np.array([point1]),
        *[
            np.array([[
                random.randint(1, image.shape[1]),
                random.randint(1, image.shape[0])
            ]])
            for _ in range(number_of_random_points)
        ],
        np.array([point1])
    ], dtype=np.int32)
]

if random.randint(0, 1):  # Either fills the shape or just draws the outline
    image = cv2.polylines(
        image,
        points,
        True,
        (0, 0, 255),
        2
    )
else:
    image = cv2.fillPoly(
        image,
        points,
        (0, 0, 255),
    )


cv2.imshow('Test', image)
cv2.waitKey()
cv2.destroyAllWindows()
