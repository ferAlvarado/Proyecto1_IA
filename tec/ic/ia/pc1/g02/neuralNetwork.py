import numpy as np
import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt
import time
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import tensorflow
from keras import *

import os
import sys
import csv
import random
import unittest
from main import *
os . system('ls -lah')


seed = 155
np.random.seed(seed)
print(np)
##
### load pima indians dataset
##
### download directly from website

dataset = pd.read_csv('testfile.csv', encoding='cp1252',header=None).values
print(dataset)

### import from local directory
###dataset = pd.read_csv("pima-indians-diabetes.data", header=None).values
##dataset
##X_train, X_test, Y_train, Y_test = train_test_split(dataset[:,0:8], dataset[:,8], 
##                                                    test_size=0.25, random_state=87)
##
##np.random.seed(seed)
##my_first_nn = Sequential() # create model
##my_first_nn.add(Dense(5, input_dim=8, activation='relu')) # hidden layer
##my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
##my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
##
##from keras.callbacks import ModelCheckpoint
### specify filepath- this will write a new file for each epoch with the epoch number contained within the filename
##filepath="nn_weights-{epoch:02d}.hdf5"
##checkpoint = keras.callbacks.ModelCheckpoint(filepath, monitor='val_acc', verbose=0, 
##                                             save_weights_only=False, save_best_only=False, mode='max')
##
##
##my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=1000, verbose=0, batch_size=X_train.shape[0],
##                                     callbacks=[checkpoint], initial_epoch=0)
##
##
### [loss, accuracy]
##my_first_nn.evaluate(X_test, Y_test, verbose=0)
##[my_first_nn_fitted.history['loss'][0:5], my_first_nn_fitted.history['acc'][0:5]]
##
##temp_test_model = Sequential() # create model
##temp_test_model.add(Dense(5, input_dim=8, activation='relu')) # hidden layer
##temp_test_model.add(Dense(1, activation='sigmoid')) # output layer
##temp_test_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
##test_over_time = []
##for i in range(len(my_first_nn_fitted.history['acc'])):
##    temp_test_model.load_weights("nn_weights-%02d.hdf5" % i)
##    scores = temp_test_model.evaluate(X_test, Y_test, verbose=0)
##    # 0 is loss; 1 is accuracy
##    test_over_time.append(scores)
##
##
##
##def runNN(X_train_set, Y_train_set, X_test_set, Y_test_set, n_neurons, n_epochs, seed=155,
##          history=True, del_files=True, validation_split=0.0, early_stopping=None):
##
##my_second_nn = runNN(X_train, Y_train, X_test, Y_test, 1000, 1000)
##
##
##scaler = StandardScaler()
##nn_output_unscaled = runNN(X_train, Y_train, X_test, Y_test, 1000, 1000)
##nn_output_scaled = runNN(scaler.fit_transform(X_train), Y_train, 
##                         scaler.fit_transform(X_test), Y_test, 1000, 1000)
##
##nn_output_scaled['acc'][-1]
##
##
##early_stop_crit = keras.callbacks.EarlyStopping(monitor='val_loss', min_delta=0, 
##                                                patience=20, verbose=0, mode='auto')
##nn_output_unscaled = runNN(X_train, Y_train, X_test, Y_test, 1000, 1000,
##                                         validation_split=0.2, early_stopping=early_stop_crit)
##nn_output_scaled = runNN(scaler.fit_transform(X_train), Y_train, scaler.fit_transform(X_test), 
##                         Y_test, 1000, 1000,validation_split=0.2, early_stopping=early_stop_crit)
