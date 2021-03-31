import cv2

# 사이즈 조절
img = cv2.imread("image/KakaoTalk_20210325_113630664_09.jpg")
print("img.shape = {0}".format(img.shape))

resize_img = cv2.resize(img, (500, 500))
print("resize_img.shape = {0}".format(resize_img.shape))

cv2.imshow("img", img)
cv2.imshow("resize img", resize_img)
cv2.waitKey()

# 출력
# img.shape = (360, 480, 3)
# resize_img.shape = (300, 300, 3)ㅍ