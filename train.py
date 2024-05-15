import numpy as np
import cv2 as cv
import mtcnn
import matplotlib.pyplot as plt
import tensorflow as tf
import os
from mtcnn import MTCNN
from keras_facenet import FaceNet
import face_functions as fp
import sklearn
import joblib
from face_functions import *


embedder = FaceNet()
def embedding_(img):
    img = [i for i in img if i is not None]
    img = np.asarray(img)
    img = img.astype('float32')
    img = np.expand_dims(img, axis=0)
    yhat = embedder.embeddings(img)
    return yhat[0]


def add_person(ID):
    X_train = []
    Y_train = []
    k =ID
    for i in range(1,k+1):
        X,Y = detect_face(i)
        for img in X:
            X_train.append(embedding_(img))
        for j in Y:
            Y_train.append(j)
    X_train = np.asarray(X_train)
    Y_train = np.asarray(Y_train)
    print("Shape of x and y is : ",X_train.shape,Y_train)
    return X_train,Y_train 
    
def train_model(X_train,Y):
    #SVM Model
    from sklearn.svm import SVC
    model = SVC(kernel='linear', probability=True)
    model.fit(X_train, Y)
    # Save the model
    joblib.dump(model, 'model_2.joblib')
    print("Model saved successfully!")
    
