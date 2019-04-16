import cv2
import numpy as np
from PIL import Image
import pymysql
import pymysql.cursors
#conn=pymysql.connect(host='localhost',user='root',password='12345678',db='mayank')
#a=conn.cursor()
def dwebcam():
    

    recognizer1 = cv2.face.LBPHFaceRecognizer_create()
    recognizer1.read("recognizer\\trainner.yml")
    cascadePath = 'haarcascade_frontalface_default.xml'
    faceCascade = cv2.CascadeClassifier(cascadePath);

# http://192.168.137.161:8080/video
    cam = cv2.VideoCapture(0)
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    fontColor = (255, 255, 255)
    while (True):
        ret,im =cam.read();
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.25,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id,conf=recognizer1.predict(gray[y:y+h,x:x+w])
            print(Id)
            #k=int(Id)
            #a.execute('select name from nametable where id=%s',(k))
            #print(a.fetchone())
            #name1=str(a.fetchone()[0])
            
            if(conf<75):
                #n=name1
            
       
                if(Id==2):
                    Id="Mayank"
                elif(Id==3):
                    Id="sachin" 
                elif (Id==4):
                    Id="deepak"
            
                
                elif(Id==6):
                    Id="Sir"
                elif(Id==11):
                    Id="pankaj_sir"
            else:
                Id="Unknown"
        
 
       
        
        
       
            cv2.putText(im,str(Id), (x,y+h),fontFace,fontScale,fontColor)
        cv2.imshow('im',im) 
        if (cv2.waitKey(1)==ord('q')):
            break;
    cam.release()
    cv2.destroyAllWindows()
#dwebcam()
