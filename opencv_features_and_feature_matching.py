import cv2

camera = cv2.VideoCapture(1)
reference_image = cv2.imread("Images/image_features/pencil_sharpener.jpg")
reference_gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)
reference_sift = cv2.SIFT_create()
reference_kp, reference_des = reference_sift.detectAndCompute(reference_gray, None)

# The first argument can be cv2.NORM_L1, cv2.NORM_L2, cv2.NORM_HAMMING, and cv2.NORM_HAMMING2
# cv2.NORM_L1 or cv2.NORM_L2 for sift, with cv2.NORM_L1 being faster but less accurate than cv2.NORM_L2.
# cv2.NORM_HAMMING should be used with ORB, BRISK, or BRIEF. Under most circumstances you won't need to use cv2.NORM_HAMMING2.
# The first argument is an image of the object you are trying to detect.
bf_matcher = cv2.BFMatcher(cv2.NORM_L2, False)

number = 0

while True:
    ret, image = camera.read()
    if not ret or image is None:
        continue

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sift = cv2.SIFT_create()
    current_kp, current_des = sift.detectAndCompute(gray, None)
    # You can use the following 2 lines instead of the above line, but there is no difference.
    # kp = sift.detect(gray)
    # kp, des = sift.compute(gray)
    if current_des is None:
        continue

    keypoints_img = cv2.drawKeypoints(gray, current_kp, None,
                                      flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # cv2.imshow("Keypoints", keypoints_img)

    matches = sorted(bf_matcher.match(reference_des, current_des), key=lambda match: match.distance)
    object_center_lst = [current_kp[match.trainIdx].pt for match in matches]
    object_center_x = sum([item[0] for item in object_center_lst]) / len(object_center_lst)
    object_center_y = sum([item[1] for item in object_center_lst]) / len(object_center_lst)
    print(object_center_x, object_center_y)

    image = cv2.circle(image, (round(object_center_x), round(object_center_y)), 15, (255, 0, 0), -1)

    img = cv2.drawMatches(reference_image, reference_kp, image, current_kp, matches, None)

    cv2.imshow("Final Image", img)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('s'):
        cv2.imwrite(f"Images/image_features/image{number}.jpg", image)
        number += 1
