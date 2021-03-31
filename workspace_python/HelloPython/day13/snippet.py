import cv2
import numpy as np
#회색 

arr = [
        [0,1,1,1,0],
        [0,1,1,1,0],
        [0,1,1,1,0],
        [0,1,1,1,0],
        [0,1,1,1,0]
    ]

arr_n = np.array(arr)*255
print(arr_n)

cv2.imwrite('image/test.png', arr_n) 

cv2.waitKey(0) 
cv2.destroyAllWindows()
