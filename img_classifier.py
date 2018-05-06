# -*- coding: utf-8 -*-
"""
Created on Sun May  6 12:41:13 2018

@author: SIVA-PC
"""

#train image classifier with tensor flow code

from sklearn import cross_validation,metrics
import tensorflow as tf
from tensorflow.contrib import learn
def main(unused_in):
    #load dataset
    iris=learn.datasets.load_dataset('iris')
    x_train,y_train,x_test,y_test=cross_validation.train_test_split(iris.data,iris.target,test_size=.2,random_state=42)
    #build 3 layer DNN with 10,20,10 hidden layers
    clasifier=learn.DNNClassifier(hidden_units=[10,20,10],n_classes=3)
    #fit and predict
    clasifier.fit(x_train,y_train,steps=200)
    score=metrics.accuracy_score(y_test,clasifier.predict(x_test))
    print("accuracy:{0:f}".format(score))
        