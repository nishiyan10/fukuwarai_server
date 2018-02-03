import numpy as np
import cv2


face_cascade = cv2.CascadeClassifier('cascade_file/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('cascade_file/haarcascade_eye.xml')

nose_cascade = cv2.CascadeClassifier("cascade_file/haarcascade_mcs_nose.xml");

mouth_cascade = cv2.CascadeClassifier("cascade_file/haarcascade_mcs_mouth.xml");



def enm(trim_face,eyes,noserect,mouthrect):
    eyecount = 0

    data = {
        "eyel" : None,
        "eyer" : None,
        "nose" : None,
        "mouth": None
    }

    for rect in eyes:
        if eyecount == 0:
            x = rect[0]
            y = rect[1]
            w = rect[2]
            h = rect[3]
            data["eyel"] = {
                "img" : cv2.imencode( '.jpg' , trim_face[y:y+h,x:x+w]),
                "w"   : w,
                "h"   : h
            }

        elif eyecount == 1:
            x = rect[0]
            y = rect[1]
            w = rect[2]
            h = rect[3]
            data["eyer"] = {
                "img" : cv2.imencode( '.jpg' , trim_face[y:y+h,x:x+w]),
                "w"   : w,
                "h"   : h
            }
        eyecount += 1

        for rect in noserect:
            x = rect[0]
            y = rect[1]
            w = rect[2]
            h = rect[3]
            data["nose"] = {
                "img" : cv2.imencode( '.jpg' , trim_face[y:y+h,x:x+w]),
                "w"   : w,
                "h"   : h
            }

        for rect in mouthrect:
            x = rect[0]
            y = rect[1]
            w = rect[2]
            h = rect[3]
            data["mouth"] = {
                "img" : cv2.imencode( '.jpg' , trim_face[y:y+h,x:x+w]),
                "w"   : w,
                "h"   : h
            }

    return data
    

def face(image,image_gray,facerect):
    size = (300,300)
    for rect in facerect:
        
        x = rect[0]
        y = rect[1]
        w = rect[2]
        h = rect[3]
        image = image[y-30:y+h+10, x:x+w]
        image = cv2.resize(image, size, interpolation = cv2.INTER_CUBIC)
        
        trim_face = image

        return trim_face



def readImageFW(image):
    
    size = (800,800)
    image = cv2.resize(image, size, interpolation = cv2.INTER_CUBIC)

    print(image, flush=True)
    
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    facerect = face_cascade.detectMultiScale(image_gray, 1.1, 5)
    
    trim_face = face(image,image_gray,facerect)
    
    
    eyes = eye_cascade.detectMultiScale(trim_face)
    
    noserect = nose_cascade.detectMultiScale(trim_face)
    
    mouthrect = mouth_cascade.detectMultiScale(trim_face)
    
    return enm(trim_face,eyes,noserect,mouthrect)