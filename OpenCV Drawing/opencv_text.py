import cv2

image = cv2.imread("../Images/RPi_Image.png")


image = cv2.putText(
    image,
    "Test Text",
    (50, 50),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.5,
    (0, 0, 0),
    thickness=2
)
"""
Parameters:
==========
@param img Image.
@param text Text string to be drawn.
@param org Bottom-left corner of the text string in the image.
@param fontFace Font type, see #HersheyFonts.
@param fontScale Font scale factor that is multiplied by the font-specific base size.
@param color Text color.
@param thickness Thickness of the lines used to draw a text. Must be greater than zero.
@param lineType Line type. See #LineTypes
@param bottomLeftOrigin When true, the image data origin is at the bottom-left corner. Otherwise, it is at the top-left corner.

Valid fonts for fontFace:
cv2.FONT_HERSHEY_SIMPLEX
cv2.FONT_HERSHEY_PLAIN
cv2.FONT_HERSHEY_DUPLEX
cv2.FONT_HERSHEY_COMPLEX
cv2.FONT_HERSHEY_TRIPLEX
cv2.FONT_HERSHEY_COMPLEX_SMALL
cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cv2.FONT_HERSHEY_SCRIPT_COMPLEX

The fontScale argument is the final size divided by the default size of the font.
"""

cv2.imshow("OpenCV Text", cv2.resize(image, (550, 535)))
cv2.waitKey()

cv2.destroyAllWindows()
