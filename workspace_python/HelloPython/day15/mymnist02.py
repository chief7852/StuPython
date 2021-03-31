from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical

# MNIST 데이터셋 불러오기
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
arr = train_images[1]


for i in arr:
    for j in i:
        if j == 0:
            print("0",end="")
        else:
            print("1",end="")
    print()    
    