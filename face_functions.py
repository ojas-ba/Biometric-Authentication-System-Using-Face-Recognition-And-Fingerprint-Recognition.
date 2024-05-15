import numpy as np
import cv2 as cv
import mtcnn
import matplotlib.pyplot as plt
import tensorflow as tf
import os 
from  mtcnn import MTCNN


# Function creates folder everytime a new Face is Added for that persons_images

detector = MTCNN()

# Function to detect faces using MTCNN and give us 160x160 image of the face which will then be fed to FaceNet.
def detect_face(ID):
    img_folder = "C:\EEX_Authentication_system\input_faces"
    img_folder_person = os.path.join(img_folder,"Person_"+str(ID))
    list_faces = []
    label=[]
    for i in os.listdir(img_folder_person):
        img_path = os.path.join(img_folder_person,i)
        print(i)
        if os.path.isfile(img_path): # isfile checks if path points to imagefile.
            img =cv.imread(img_path)
            if img is not None:
                img =cv.cvtColor(img, cv.COLOR_BGR2RGB) # converting to RGB
                faces = detector.detect_faces(img)
                if faces:
                    x,y,w,h = faces[0]['box']
                    x, y, w, h = max(0, x), max(0, y), max(0, w), max(0, h) #making sure non negative co-ordinates
                    img= cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                    img = img[y:y+h,x:x+w] # here we are selecting the face region x,x+w and y,y+h are the cordinates of them given by mtcnn
                    final_img =cv.resize(img,(160,160))
                    final_img = cv.cvtColor(final_img, cv.COLOR_RGB2BGR)
                    final_img = np.asarray(final_img)
                    list_faces.append(final_img)
                    label.append("Person_"+str(ID))
    return list_faces,label

def take_photos_input(count):
    count+=1
    ID = count
    folder_ = "C:\EEX_Authentication_system\input_faces"
    img_folder = os.path.join(folder_,"Person_"+str(ID))
    os.makedirs(img_folder,exist_ok=True)
    cap = cv.VideoCapture(0)
    num_imgs = 45
    for i in range(num_imgs):
        check_frame, img = cap.read()
        if not check_frame:
            break
        output=os.path.join(img_folder,f"Image_{i}.jpg")
        cv.imwrite(output,img)
    cap.release()
    cv.destroyAllWindows()
    print("Id is :",ID)
    return ID

def cap_face():
    cap = cv.VideoCapture(0)
    img = cap.read()
    return np.array(img[1])

def pre_process_img(img):
   if img is not None:
        img =cv.cvtColor(img, cv.COLOR_BGR2RGB) # converting to RGB
        faces = detector.detect_faces(img)
        if faces:
            x,y,w,h = faces[0]['box']
            x, y, w, h = max(0, x), max(0, y), max(0, w), max(0, h) #making sure non negative co-ordinates
            img= cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            img = img[y:y+h,x:x+w] # here we are selecting the face region x,x+w and y,y+h are the cordinates of them given by mtcnn
            final_img = cv.resize(img,(160,160))
            final_img = cv.cvtColor(final_img, cv.COLOR_RGB2BGR)
            final_img = np.asarray(final_img)
            return final_img