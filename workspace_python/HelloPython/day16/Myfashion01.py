import tensorflow as tf
import numpy as np
import cv2
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

predictions = model.predict(test_images)

cnt_o = 0
cnt_x = 0 

for i,p in enumerate(predictions):
    val_p = np.argmax(p)
    val_g = test_labels[i]
    if val_p == val_g:
        cnt_o +=1
    else : 
        cnt_x +=1
        cv2.imwrite("diff/"+class_names[val_p]+"_"+class_names[val_g]+"_"+str(i)+".jpg", test_images[i]*255)


print("같음"+str(cnt_o))
print("다름"+str(cnt_x))

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\nTest accuracy:', test_acc)