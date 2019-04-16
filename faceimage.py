mport cv2
import numpy as np
from PIL import Image
import easygui
import pymysql
import pymysql.cursors
#conn=pymysql.connect(host='localhost',user='root',password='12345678',db='mayank')
#a=conn.cursor()
def inimage():
    
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('recognizer/trainner.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
#im1 = Image.open('data/20180329_221530.jpg')
#im = np.array(im1);
    v =(easygui.fileopenbox())

    str1=''
    for i in v:
        if(i=='EOF'):
            break
        elif(i=='\\'):
            str1=str1+'/'
        else:
            str1=str1+str(i)

    iml=cv2.VideoCapture(str(str1))
    check,im=iml.read()
    img = cv2.resize(im, (0,0), fx=0.5, fy=0.5)
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    fontColor = (255, 255, 255)


    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.16,5)

    for(x,y,w,h) in faces:
        #print(x,y,w,h)
        cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)
        Id,conf = recognizer.predict(gray[y:y+h,x:x+w])
        #sql='select name from nametable where id=Id;'
        #a.execute(sql)
        #name1=a.fetchone()[0]
        #print(conf)
        if(conf<75):
            
            
            #n=name1
        
            if(Id==2):
                Id="Mayank"
            elif(Id==3):
                Id="sachin"
            elif(Id==4):
                Id="deepak"
            elif(Id==5):
                Id="Mayank"
            elif(Id==6):
                Id="Sir"
               
             
        else:
                Id="Unknown"
        cv2.putText(img,str(Id), (x,y+h),fontFace,fontScale,fontColor)
    cv2.imshow('im',img)
    if cv2.waitKey(10) & cv2.waitKey(0) == ord('q') :
        cv2.destroyAllWindows()
 
    
