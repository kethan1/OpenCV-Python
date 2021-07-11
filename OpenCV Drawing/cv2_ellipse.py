import cv2

image = cv2.imread("../Images/RPi_Image.png")
image = cv2.ellipse(
    image,
    (100, 100),  # Tuple with the center in (x, y) form

    (50, 30),    # Tuple with the size of the ellipse in (length / 2, width / 2) form

    0,           # Angle that the ellipse is rotated by

    0,           # Starting angle of the ellipse. Anything less than the
                 # starting angle will not be shown. 0 to cut of nothing, 360
                 # to cut off everything

    360,         # Ending angle of the ellipse. Anything less than the ending
                 # angle will not be shown. 360 to cut off nothing, and 0 to
                 # cut off everything
    (0, 255, 0),
    -1           # The thickness of the line. If -1 is passed, the figure will
                 # be filled. This parameter is optional.
)
"""
Parameters:
==========
ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]]) -> img
@param img Image.
@param center Center of the ellipse.
@param axes Half of the size of the ellipse main axes.
@param angle Ellipse rotation angle in degrees.
@param startAngle Starting angle of the elliptic arc in degrees.
@param endAngle Ending angle of the elliptic arc in degrees.
@param color Ellipse color.
@param thickness Thickness of the ellipse arc outline, if positive. Otherwise,
       this indicates that a filled ellipse sector is to be drawn.
@param lineType Type of the ellipse boundary. See #LineTypes
@param shift Number of fractional bits in the coordinates of the center and
       values of axes.

ellipse(img, box, color[, thickness[, lineType]]) -> img
@overload
@param img Image.
@param box Alternative ellipse representation via RotatedRect. This means that
       the function draws an ellipse inscribed in the rotated rectangle.
@param color Ellipse color.
@param thickness Thickness of the ellipse arc outline, if positive. Otherwise,
       this indicates that a filled ellipse sector is to be drawn
@param lineType Type of the ellipse boundary. See #LineTypes
"""

cv2.imshow("Ellipse", image)
cv2.waitKey()
cv2.destroyAllWindows()
