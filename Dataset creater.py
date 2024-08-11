import cv2
import numpy as np
import sqlite3

faceDetect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")# to detect the faces in camera

cam=cv2.VideoCapture(0) # 0 is for web camera 


#database cereation 
def insertorupdate(Id,Name,age): #function for sqllite database
    conn=sqlite3.connect("sqlite.db")#connect database
    cmd="SELECT * FROM STUDENTS WHERE ID="+str(Id)
    cursor= conn.execute(cmd); # to excute statement
    isRecordExit=0; #assume there is no record in our table  
    for row in cursor:
        isRecordExit=1;
    if (isRecordExit==1):#if there is a record exist in our table
        conn.execute("UPDATE STUDENTS SET NAME=? WHERE Id=?", (Name,Id,))
        conn.execute("UPDATE STUDENTS SET age=? WHERE Id=?",(age,Id,))
    else:#if there is no record exit we inster the values
        conn.execute('INSERT INTO STUDENTS (Id,Name,age) VALUES(?,?,?)', (Id,Name,age))
    conn.commit()
    conn.close()
#insert user defined value into table

Id=input("Enter user ID :")
Name=input("Enter user Name :")
age=input("Enter User Age :")
insertorupdate(Id,Name,age)


#detect face in web camera 

sampleNum=0
while(True):
    ret,img=cam.read()#creating two variables ret and img AND OPEN CAMERA
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converting the image to grayscale

    faces=faceDetect.detectMultiScale(gray,1.3,5)#scale factor

    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1 #if face is detected increments
        cv2.imwrite("dataset/user."+str(Id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100)
    cv2.imshow("Face",img)
    cv2.waitKey(1)
    if(sampleNum>20):
        break
cam.release() 
cv2.destroyAllWindows()
print("Welcome"+Name)






    

