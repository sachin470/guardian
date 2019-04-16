import pymysql
import pymysql.cursors
import os
import cv2
import numpy as np
#conn=pymysql.connect(host='localhost',user='root',password='12345678',db='mayank')
#a=conn.cursor()
def trainw():
    cam = cv2.VideoCapture(0)
    detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    print('enter your name')
    n=raw_input()
    
    sql='select max(id) from nametable;'
    #a.execute(sql)
    #Id=a.fetchone()[0]+1
    #c=10
    #a.execute('INSERT INTO nametable(id,name,no) VALUES (%s,%s,%s)',(Id,n,c))
    #conn.commit()
    sampleNum=0
    while(True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        #incrementing sample number 
            sampleNum=sampleNum+1
        #saving the captured face in the dataset folder
            cv2.imwrite("dataSet/User."+str(Id) +"."+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
            cv2.waitKey(100);
            cv2.imshow('frame',img)
    #wait for 100 miliseconds 
        cv2.waitKey(1)
    
    # break if the sample number is morethan 20
        if sampleNum>20:
            break;
    cam.release()
cv2.destroyAllWindows()
