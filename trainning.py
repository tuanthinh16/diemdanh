import cv2
import os.path
import numpy as np
from PIL import Image
import easygui
import cognitive_face as CF

facecascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
recongniger = cv2.face.EigenFaceRecognizer_create()
path = 'Dataset'

def getImageWithmssv(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    IDs = []
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L')
        faceNP = np.array(faceImg, 'uint8')
        print(faceNP)
        Id = int(imagePath.split('\\')[1].split('.')[1])
        faces.append(faceNP)
        IDs.append(Id)
        cv2.imshow('trainning', faceNP)
        cv2.waitKey(10)
    return faces, IDs

faces, IDs = getImageWithmssv(path)
recongniger.train(faces, np.array(IDs))
easygui.msgbox("Trainning Thành Công", title="Result")
if not os.path.exists('recongniger'):
    os.makedirs('recongniger')
recongniger.write('recongniger\\trainningdata.yml')
cv2.destroyAllWindows()