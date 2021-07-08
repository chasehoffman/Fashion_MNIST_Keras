# -*- coding: utf-8 -*-
"""assignment2FashionMNIST.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SvDl3u1551RqigvuBZnbmGCLNYKTvSCg
"""

#read this if you want to know how the data works https://keras.io/api/datasets/fashion_mnist/
#L1 and L2 regularization documentation: https://keras.io/api/layers/regularizers/
# Dropout layer documentation: https://keras.io/api/layers/regularization_layers/dropout/
#optimizer documentation: https://keras.io/api/optimizers/
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from keras.datasets import mnist
from keras.layers.core import Dense
from keras.layers import Input
from keras.models import Sequential
from keras.utils import to_categorical
from keras import optimizers
import tensorflow as tf
import tensorflow 

from tensorflow import keras

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

fig = plt.figure()
for i in range(9):
    plt.subplot(3,3,i+1)
    plt.tight_layout()
    plt.imshow(x_train[i], cmap='gray', interpolation='none')
    plt.title("Catagory: {}".format(y_train[i]))
    plt.xticks([])
    plt.yticks([])
plt.show()

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train = x_train/255
x_test = x_test/255

num_classes = 10
print('y data before: ')
print(y_train[0:5])

y_train = to_categorical(y_train, num_classes)
y_test  = to_categorical(y_test, num_classes)
print('\ny data after:')
print(y_train[0:5])

from tensorflow.keras import regularizers
from tensorflow.keras import layers
layer = layers.Dense(
    units=64,
    bias_regularizer=regularizers.l2(.025)
)

model = Sequential()
model.add(Dense(100, activation='relu', input_shape=(784,)))
model.add(Dense(100, activation='relu', input_shape=(784,)))
model.add(Dense(100, activation='relu', input_shape=(784,)))
model.add(Dense(10, activation='softmax'))

Adam = tf.keras.optimizers.Adam(learning_rate=0.0005, beta_1=0.9, beta_2=0.999, epsilon=1e-08, amsgrad=False, name="Adam")

#sgd = optimizers.SGD(lr=.1, decay=0, momentum=0.1)
model.compile(loss='categorical_crossentropy',
              optimizer=Adam,
              metrics=['accuracy'])
model.summary()

training_samples = 60000
testing_samples  = 10000

batch_size = 128
epochs     = 15

history = model.fit(x_train[:training_samples],
                    y_train[:training_samples],
                    epochs=epochs,
                    batch_size=batch_size,
                    verbose=1,
                    validation_data=(x_test[:testing_samples],y_test[:testing_samples]))
#The best convolutional model trained with this data is in the low 90's accuracy. anything over 88 is pretty good

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

plt.figure()
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])

plt.title('Model loss')
plt.ylabel('loss'); plt.xlabel('epoch')
plt.legend(('train','test'))

plt.figure()
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])

plt.title('Model accuracy')
plt.ylabel('accuracy'); plt.xlabel('epoch')
plt.legend(('train','test'))


plt.show()