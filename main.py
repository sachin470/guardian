mport demofolder
import databasebyimage
import trainner
import datasetcreater
import detector
import faceinimage
a=1
print(" WELCOME To GUARDIAN")
while(a==1):
    
    
    print("Enter 1 to train new face")
    print("Enter 2 to Detect faces")
    n=int(input())
    if(n==1):
        print("Enter 1 to train your face by webcam")
        print("Enter 2 for train face by image")
        m=int(input())
        if(m==1):
            datasetcreater.trainw()
            trainner.webcam()
        elif(m==2):
            databasebyimage.trainimage()
            trainner.webcam()
        else:
            print("not a choice")
    elif(n==2):
          print(" Enter 1 to detect face using webcam")
          print("Enter 2 to find your images inside a folder")
          print("Enter 3 to detect faces in a image")
          m=int(input())
          if(m==1):
              detector.dwebcam()
          elif(m==2):
              demofolder.folder()
          elif(m==3):
              faceinimage.inimage()
          else:
              print("wrong choice")
    else:
        print("wrong choice")
    print("Enter 1 for continue 2 for exit")
    a=int(input())
