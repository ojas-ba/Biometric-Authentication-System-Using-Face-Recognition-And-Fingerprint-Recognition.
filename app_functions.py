from verify import *
from face_functions import *
from train import *
import numpy as np
import cv2 as cv
import mtcnn
import matplotlib.pyplot as plt
import tensorflow as tf
import os
from mtcnn import MTCNN
from keras_facenet import FaceNet
import sklearn
import joblib


def add_faces(id):
    X,Y = add_person(id)
    return X,Y
    
    
    

    