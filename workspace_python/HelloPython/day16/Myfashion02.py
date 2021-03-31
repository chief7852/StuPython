import tensorflow as tf
import numpy as np
import cv2
# 인터넷에서 이미지를 끌고와서 비교해서 정답찾아라
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()



class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0
test_images = test_images / 255.0


model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10)


img = cv2.imread("sandal.jpg",1)

resize_img = cv2.resize(img, (28, 28))
image_gray = cv2.cvtColor(resize_img,cv2.COLOR_BGR2GRAY)

img_input = (255 - image_gray)/256

img_in = np.reshape(img_input,(1, 28, 28))


predictions = model.predict(img_in)
print(np.argmax(predictions[0]))




test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\nTest accuracy:', test_acc)