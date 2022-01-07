import cv2
import numpy as np
import glob
import tensorflow as tf
import tensorflow
from tensorflow.keras import datasets, layers, models

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Conv2D, MaxPool2D, Flatten
#from tensorflow.keras.utils import np_utils
from tensorflow.keras import utils


im = cv2.imread('./image_chips2/clipped_image_254.png',0)
#im2 = Image.open('./image_chips/clipped_image_1.tif.png')


print(im.shape)


'''
cv2.imshow('image', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''



image_files = glob.glob('./image_chips2/*.png')
print(image_files)


image_label = [0 for i in range(len(image_files))]
y_train = utils.to_categorical(image_label, 0)
y_train


len(image_label), len(image_files)

im.dtype


train_image = []
for i in image_files:
    im = np.array(cv2.imread(i, 0))
    train_image.append(im)


train_image = np.array(train_image)
train_image.shape



X_train = train_image / 255.

print(X_train)



'''train_image = np.expand_dims(train_image, axis=0)
print(train_image.shape)'''


'''
# building a linear stack of layers with the sequential model
model = Sequential()
# convolutional layer
model.add(Conv2D(25, kernel_size=(3,3), strides=(1,1), padding='valid', activation='relu', input_shape=(24,24,1)))
model.add(MaxPool2D(pool_size=(1,1)))
# flatten output of conv
model.add(Flatten())
# hidden layer
model.add(Dense(100, activation='relu'))
# output layer
model.add(Dense(1, activation='softmax'))

# compiling the sequential model
model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

# training the model for 10 epochs
model.fit(train_image, y_train, epochs=100)

'''


