# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rwyu-H5UCF7GSZF6x6rfyGLeCpT134G5

# libraries in DL
Theano
Keras
Tensorflow
Pytorch



# import libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns# open-source Python library built on top of matplotlib
import tensorflow as tf #a Python library for fast numerical computing created and released by Google
from tensorflow import keras#Keras is a powerful and easy-to-use free open source Python library for developing and evaluating deep learning models.

"""# importing the data 

keras as lotsof data
"""

data=keras.datasets.mnist#importing the data

data #shows the location

df=data.load_data( ) #download the data from keras and load the data
#it download in two dataset 1)training data set
#2)testing data set

print(df) #print the data set of the images ,the pixcels of the images

(X_train,Y_train),(X_test,Y_test)=df

X_train.shape #60k pics with 28 by 28 pixcels

X_test.shape

X_train[0]

plt.matshow(X_train[0])#shows the image

for i in range (10):
  plt.matshow(X_train[i])

Y_test.shape

Y_test.ndim

X_test.ndim

X_train_flat=X_train.reshape(len(X_train),28*28)
X_test_flat=X_test.reshape(len(X_test),28*28)

X_train_flat[0].ndim#for 1 image

"""#ANN module creation """

from tensorflow.keras import Sequential #Sequencial is going create the hidden layers
from tensorflow.keras.layers import Dense #this dense is going to help us to creat multiple layers 
# and the Sequencial is goint to help the store all these layers

#first_layer.
model=Sequential([
    Dense(units=10,
          input_shape=(784,),
          activation='sigmoid')
])


#while the model is train i want to know the loss during the creation
#gonnna create a optimizor to reduce the loss
# model.compile(
#     optimizer='adam',
#     loss='spares_categorical_crossentropy',#search on google
#     metrics=['accuracy']
# )

model.compile(optimizer='adam',loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])

"""#train/fit the model"""

model.fit(X_test_flat,Y_test,epochs=50)
#more the epocs higher the accuracy
#epocs means how many time does your module want to see your data

y_pred=model.predict(X_test_flat)

Y_test

X_test_flat

model.evaluate(X_test_flat,Y_test)
