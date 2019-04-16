import cv2
import glob
import numpy as np
from PIL import Image
import easygui
import pymysql
import pymysql.cursors
#conn=pymysql.connect(host='localhost',user='root',password='12345678',db='mayank')
#a=conn.cursor()
def folder():
    
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('recognizer/trainner.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
#im1 = Image.open('data/20180329_221530.jpg')
#im = np.array(im1);
#iml=cv2.VideoCapture('data/m0.jpg')
#check,im=iml.read()
    v =(easygui.diropenbox())

    str1=''
    for i in v:
        if(i=='EOF'):
            break
        elif(i=='\\'):
            str1=str1+'/'
        else:
            str1=str1+str(i)
    gimg=glob.glob(str(str1+'/*.jpg'))
    i=0
    j=0
    print("enter person id to find images")
    Id1=input()
    for timg in gimg:
        img=cv2.imread(timg)
    #img = cv2.resize(im, (0,0), fx=0.5, fy=0.5)
        fontFace = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        fontColor = (255, 255, 255)
    

        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.20,5)

        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)
            Id,conf = recognizer.predict(gray[y:y+h,x:x+w])
            print(Id)
            #sql='select name from nametable where id=Id;'
            #a.execute(sql)
            #name1=a.fetchone()[0]
            if(conf<75):
                
                '''if(name1==n):
                    i=i+1
                    cv2.imwrite("dataSet1/User."+str(name1)+"."+str(i) + ".jpg", img)'''
                    
                
                if Id==Id1:
                    
            
                    i=i+1
                    cv2.imwrite("dataSet1/User."+str(Id)+"."+str(i) + ".jpg", img)
                
                              
                print(Id)
                cv2.putText(img,str(Id), (x,y+h),fontFace,fontScale,fontColor)
        #cv2.imshow('im',img)
   

            
        if (cv2.waitKey(1)==ord('q')):
            break
    cv2.destroyAllWindows()
