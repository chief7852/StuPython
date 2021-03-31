import cv2

#회전 세밀하게
img = cv2.imread("image/KakaoTalk_20210325_113630664_05.jpg", 1)
if img is None:
    print('Image load failed!')
    img.exit()

cp = (img.shape[1] / 2, img.shape[0] / 2) # 영상의 가로 1/2, 세로 1/2
rot = cv2.getRotationMatrix2D(cp, 0, 1) # 20도 회전, 스케일 0.5배

dst = cv2.warpAffine(img, rot, (0, 0))
cv2.imshow("test", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
