import cv2

#RGB가 아니라 BGR로 색상을 준다
image = cv2.imread("image/KakaoTalk_20210325_113630664_05.jpg", 1)
print(image)

cv2.imshow("test", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
