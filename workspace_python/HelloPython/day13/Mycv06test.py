import cv2  # openCV의 패키지명
import numpy as np

def ImageWrite():
    imgFile = 'image/KakaoTalk_20210325_113630664_05.jpg'

    img = cv2.imread(imgFile, cv2.IMREAD_GRAYSCALE)

    cv2.namedWindow('test',cv2.WINDOW_NORMAL)
    cv2.imshow('test', img)

    test = cv2.waitKey(0)
    print(test)
    if( test == 97):
        cv2.imwrite('image/grayImage.jpg',img)
        cv2.destroyAllWindows()
    elif(test == 113):
        cv2.destroyAllWindows()

ImageWrite()


