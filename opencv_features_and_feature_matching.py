import cv2

camera = cv2.VideoCapture(0)
image2 = cv2.imread("Images/image_features/image1.jpg")
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
sift2 = cv2.xfeatures2d.SIFT_create()
kp2, des2 = sift2.detectAndCompute(gray2, None)

number = 0

while True:
    ret, image = camera.read()
    if not ret:
        continue

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d.SIFT_create()
    kp, des = sift.detectAndCompute(gray, None)
    # You can use the following 2 lines instead of the above line, but there is no difference.
    # kp = sift.detect(gray)
    # kp, des = sift.compute(gray)
    img = gray.copy()
    keypoints_img = cv2.drawKeypoints(gray, kp, None,
                                      flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imshow("Keypoints", keypoints_img)

    # The first argument can be cv2.NORM_L1, cv2.NORM_L2, cv2.NORM_HAMMING, and cv2.NORM_HAMMING2
    # cv2.NORM_L1 or cv2.NORM_L2 for sift, with cv2.NORM_L1 being faster but less accurate than cv2.NORM_L2.
    # cv2.NORM_HAMMING should be used with ORB, BRISK, or BRIEF. Under most circumstances you won't need to use cv2.NORM_HAMMING2.
    bf_matcher = cv2.BFMatcher(cv2.NORM_L1, False)
    # The first argument is an image of the object you are trying to detect.
    # The second argument is the image you are trying to find the image in.
    matches = bf_matcher.match(des2, des)
    matches = sorted(matches, key=lambda x: x.distance)

    img = cv2.drawMatches(image2, kp2, image, kp, matches, None)

    cv2.imshow("my image123", img)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('s'):
        cv2.imwrite(f"Images/image_features/image{number}.jpg", image)
        number += 1
