
from keras.models import load_model
import numpy as np
import cv2

img = cv2.imread("1.jpg",1)

resize_img = cv2.resize(img, (28, 28))
image_gray = cv2.cvtColor(resize_img,cv2.COLOR_BGR2GRAY)

img_input = (255 - image_gray)/256

img_in = np.reshape(img_input,(1,28*28))

model = load_model('mymodel.h5')
predictions = model.predict(img_in)


print(np.argmax(predictions))
cv2.waitKey(0)
cv2.destroyAllWindows()