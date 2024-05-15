import joblib
from face_functions import *
from train import *
#This  captures the photos for verification

def verify():
    img = cap_face()
    img = pre_process_img(img)
    img = embedding_(img)
    model = joblib.load('model_2.joblib')
    img = img.reshape(1,-1)
    result = model.predict_proba(img)[0]
    print(result)
    result = list(result)
    with open ('people.txt',"r") as f:
        global people
        people = f.read().split(',')
    if(max(result)<0.5):
        return "Not Found"
    else:
        return people[result.index(max(result))]

