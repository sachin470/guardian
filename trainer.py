import pymysql
import pymysql.cursors
import os
import cv2
import numpy as np
from PIL import Image
recognizer1 = cv2.face.LBPHFaceRecognizer_create();
def webcam():
    
    path='dataSet'
    detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml"); 
    def getImagesAndLabels(path):
    #get the path of all the files in the folder
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    
    #create empth face list
        faces=[]
    #create empty ID list
        IDs=[]
    #now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
        #loading the image and converting it to gray scale
            faceImg=Image.open(imagePath).convert('L');
        #Now we are converting the PIL image into numpy array
            faceNp=np.array(faceImg,'uint8')
        #getting the Id from the image
            ID=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
            face=detector.detectMultiScale(faceNp)
        
        #If a face is there then append that in the list as well as Id of it
        
            print ID
            for (x,y,w,h) in face:
                faces.append(faceNp[y:y+h,x:x+w])
                IDs.append(ID)
        
            cv2.imshow("training",faceNp)
            cv2.waitKey(10)
        return IDs,faces


    Ids,faces = getImagesAndLabels(path)
    recognizer1.train(faces, np.array(Ids))
    recognizer1.save('recognizer/trainner.yml')
cv2.destroyAllWindows()
