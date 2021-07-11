import cv2
import numpy

input_image: numpy.ndarray = cv2.imread("Images/RPi_Image.png", cv2.IMREAD_GRAYSCALE)
# There is also cv2.circle and cv2.polylines
grayscale_image_with_rectangle: numpy.ndarray = cv2.rectangle(
    # Input Image
    cv2.cvtColor(input_image, cv2.COLOR_GRAY2BGR),
    # Upper Left Corner
    (175, 70),
    # Lower Right Corner
    (815, 850),
    # Color
    (0, 0, 255),
    # Border
    2
)

cv2.imshow("Grayscale Image with Rectangle", cv2.resize(grayscale_image_with_rectangle, (550, 535)))
cv2.waitKey()
cv2.destroyAllWindows()

# For the second argument, 1 for vertical flip and use a 0 for horizontal flip.
cv2.imshow("Image Flipped Horizontally", cv2.resize(cv2.flip(input_image, 0), (550, 535)))
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow(
    "Image Flipped Vertically (Image is symmetrical)",
    cv2.resize(cv2.flip(input_image, 1), (550, 535))
)
cv2.waitKey()
cv2.destroyAllWindows()

input_image_copy: numpy.ndarray = input_image.copy()
#               y1:y2 x1:x2
input_image_copy[0:60, 0:60] = 1  # Use img[y1:y2, x1:x2] = (b, g, r) for color image
cv2.imshow(
    "Image Copied and Modified",
    cv2.resize(cv2.flip(input_image, 1), (550, 535))
)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow(
    "Resize Image by Side Lengths",
    cv2.resize(input_image, (550, 535))
)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow(
    "Resize Image by Scale Factor",
    cv2.resize(input_image, (0, 0), fx=0.5, fy=0.5)
)
cv2.waitKey()

cv2.destroyAllWindows()

"""
Because OpenCV images are numpy arrays we can manipulate then in anyway that
we can manipulate a numpy array. Some useful operation that we can do with
numpy arrays:

img[y, x]  # Get the value of a pixel at the coordinates x, y

img[y, x] = (b, g, r)  # Sets the pixel at the coordinate (x, y) to the color
                        (b, g, r). b, g, and r are integers between 0 and 255.
                        If the image was a grayscale image, (b, g, r) would be
                        replaced by just one integer from 0 to 255

img[y1, x1] = img[y2, x2]  # Sets the pixel at the coordinate (x1, y1) to the
                            pixel at coordinate (x2, y2)

img[y1:y2, x1:x2]  # Gets part of the image from the points (x1, y1) to
                    (x2, y2)

img[y1:y2, x1:x2] = (b, g, r)  # Sets an ROI to be the BGR color (b, g, r).
                                Use one integer between 0 and 255 if the image
                                is grayscale.

img[y1:y2, x1:x2] = img[y3:y4, x3:x4]  # Sets a section of the image with the
                                        points (x1, y1) and (x2, y2) to another
                                        section of the image with the points
                                        (x3, y3) and (x4, y4). Both sections of
                                        the images have to have the area shape.

img.shape  # Returns a tuple in this format: (height, width, length of color
            value per pixel) Here is an example: (1080, 1920, 3). This means
            that the resolution of the image is 1920 by 1080. It also means
            that the number of color values per pixel is 3. In this case, this
            is because the image is in the BGR format, which requires 3 color
            values. If it was in the grayscale format, it would only require
            one value.
"""
