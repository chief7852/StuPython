import cv2
import numpy as np

# 사이즈 조절
img = cv2.imread("fashion.png",1)

resize_img = cv2.resize(img, (28, 28))
image_gray = cv2.cvtColor(resize_img,cv2.COLOR_BGR2GRAY)

img_input = (255 - image_gray)/256

img_in = np.reshape(img_input,(1,28*28))

print(img_in)
print(img_in.shape)

cv2.imshow("1_1 img", img_input)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 출력
# img.shape = (360, 480, 3)
# resize_img.shape = (300, 300, 3)ㅍ