import numpy as np
import cv2


face_cascade = cv2.CascadeClassifier('cascade_file/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('cascade_file/haarcascade_eye.xml')

               
def face(image,image_gray,facerect):
        x = facerect[0]
        y = facerect[1]
        w = facerect[2]
        h = facerect[3]
        size = (300,300)
        img  = image[y-30:y+h+10, x:x+w]
        trim_face = cv2.resize(img, size, interpolation = cv2.INTER_CUBIC)
        eye   = trim_face[  0:150]
        nose  = trim_face[150:210]
        mouth = trim_face[210:300]

        return {
            "eye"  : cv2.imencode( '.jpg' ,   eye ),
            "nose" : cv2.imencode( '.jpg' ,  nose ),
            "mouth": cv2.imencode( '.jpg' , mouth )
        }

def readImageRL(image):
    size = (800,800)
    image = cv2.resize(image, size, interpolation = cv2.INTER_CUBIC)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    facerect = face_cascade.detectMultiScale(image_gray, 1.1, 5)
    return face(image,image_gray,facerect)