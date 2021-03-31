import cv2

#이미지 색 변경(numpy구조)
image = cv2.imread("image/ato.jpg",1 )
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
print(image_gray)

cv2.imshow("test", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
