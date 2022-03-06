# from turtle import shape
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.utils import to_categorical 
import tensorflow as tf
import numpy as np
from keras import backend as K
####Column 1 means bad and column 2 means good
df = pd.read_csv('data.csv')
df = df.sample(frac = 1)
properties = list(df.columns.values)
properties.remove('output')
X = df[properties]
y = df['output']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.40, random_state=40)
print(X_train.shape)
print(X_test.shape)

# print(y_test)
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
# print(y_test)

count_classes = y_test.shape[1]
print(count_classes)

model = Sequential()
model.add(Dense(20, activation='relu', input_dim=36))
model.add(Dense(10, activation='relu'))
model.add(Dense(5, activation='relu'))
model.add(Dense(2, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=100, batch_size=32)

pred_train= model.predict(X_train)
scores = model.evaluate(X_train, y_train)
print('Accuracy on training data: {}% \n Error on training data: {}'.format(scores[1]*100, 1 - scores[1]))   

pred_test= model.predict(X_test)
scores2 = model.evaluate(X_test, y_test)
print('Accuracy on test data: {}% \n Error on test data: {}'.format(scores2[1]*100, 1 - scores2[1]))    

model.save("classifier")
model.save("classifier.h5")

# sample = ['1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '1', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0']
# sample1 = [int(k) for k in sample]

# out = model.predict([sample1])
# print(out)