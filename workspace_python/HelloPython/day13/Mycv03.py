import cv2

#90도 회줜
img = cv2.imread("image/ato.jpg", 1)
img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
print(img_rotate_90_clockwise)

cv2.imshow("test", img_rotate_90_clockwise)
cv2.waitKey(0)
cv2.destroyAllWindows()
