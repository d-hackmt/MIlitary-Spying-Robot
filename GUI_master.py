import tkinter as tk
from tkinter import * 
from tkinter import ttk, LEFT, END
import time
import numpy as np
import cv2
import os
from PIL import Image , ImageTk     
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 

##############################################+=============================================================

root = tk.Tk()
root.configure(background="seashell2")
#root.geometry("1300x700")
import sqlite3
my_conn = sqlite3.connect('face.db')

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Person Identification Using Face Detection")


#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('Face.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)


lbl = tk.Label(root, text="Person Identification Using Face Detection", font=('times', 30,' bold '), height=1, width=40,bg="Black",fg="indian red")
lbl.place(x=330, y=5)

frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=280, height=600, bd=5, font=('times', 15, ' bold '),bg="seashell4")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=5, y=50)

#frame_display = tk.LabelFrame(root, text=" --Display-- ", width=900, height=250, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display.grid(row=0, column=0, sticky='nw')
#frame_display.place(x=330, y=100)
################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 


def Create_database():
        
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    cap = cv2.VideoCapture(0)
    
#    id = input('enter user id')
    id=entry2.get()
    
    sampleN=0;
    
    while 1:
    
        ret, img = cap.read()
    
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
        for (x,y,w,h) in faces:
    
            sampleN=sampleN+1;
    
            cv2.imwrite("facesData/User."+str(id)+ "." +str(sampleN)+ ".jpg", gray[y:y+h, x:x+w])
    
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
            cv2.waitKey(100)
    
        cv2.imshow('img',img)
    
        cv2.waitKey(1)
    
        if sampleN > 60:
    
            break
    
    cap.release()
    entry2.delete(0,'end')
    cv2.destroyAllWindows()

def otp():
    print("OTP Generation process")
    ''' from subprocess import call
    call(['python3', 'first.py'])'''
    import first.py

def Train_database():
           
    recognizer =cv2.face.LBPHFaceRecognizer_create();
    
    path="facesData"
    
    def getImagesWithID(path):
    
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]   
    
     # print image_path   
    
     #getImagesWithID(path)
    
        faces = []
    
        IDs = []
    
        for imagePath in imagePaths:      
    
      # Read the image and convert to grayscale
    
            facesImg = Image.open(imagePath).convert('L')
    
            faceNP = np.array(facesImg, 'uint8')
    
            # Get the label of the image
    
            ID= int(os.path.split(imagePath)[-1].split(".")[1])
    
             # Detect the face in the image
    
            faces.append(faceNP)
    
            IDs.append(ID)
    
            cv2.imshow("Adding faces for traning",faceNP)
    
            cv2.waitKey(10)
    
        return np.array(IDs), faces
    
    Ids,faces  = getImagesWithID(path)
    
    recognizer.train(faces,Ids)
    
    recognizer.save("trainingdata.yml")
    
    cv2.destroyAllWindows()

def Test_database():
    global id
    flag=0
    recognizer = cv2.face.LBPHFaceRecognizer_create(1, 8, 8, 8, 100)
#    recognizer = cv2.face.FisherFaceRecognizer(0, 3000);
    
    recognizer.read('trainingdata.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    font = cv2.FONT_HERSHEY_SIMPLEX
    #iniciate id counter
    id = 0
    # names related to ids: example ==> Marcelo: id=1,  etc
    names = ['None', 'Mrunalini', 'Aniruddha', 'Vinod Sir'] 
    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height
    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    
    while True:
        ret, img =cam.read()
#       img = cv2.flip(img, -1) # Flip vertically
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray,1.3,8,minSize = (int(minW), int(minH)))

        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            print("con",confidence)
                
            
            # If confidence is less them 100 ==> "0" : perfect match
            
            if (confidence < 50):
                print("Auth")
               
                id = "Face authenticated"
                #name = names[id]
                print(type(id))
             
                confidence = "  {0}%".format(round(100 - confidence))
                print(confidence)
                
                         
                cv2.putText(img,str(id),(x+5,y-5),font,1,(255,255,255),2)
                cv2.putText(img,str(confidence),(x+5,y+h-5),font,1,(255,255,0),1)
                cam.release()
                cv2.destroyAllWindows()
                label_1 = tk.Label(root, text="Face authenticated Successfully...",font=("bold", 20),bg="pink",fg="Black")
                label_1.place(x=500,y=100)
                
            else:

                id = "unknown Person Identified"
                print(id)
                confidence = "  {0}%".format(round(100 - confidence))
                print(confidence)
                cv2.putText(img,str(id),(x+5,y-5),font,1,(255,255,255),2)
                cv2.putText(img,str(confidence),(x+5,y+h-5),font,1,(255,255,0),1)  
                cam.release()
                cv2.destroyAllWindows()
                label_3 = tk.Label(root, text="Ooopsss...unknown Person Identified..",font=("bold", 20),bg="red",fg="Black")
                label_3.place(x=500,y=100)
                
        

#        time.sleep(0.2)
        cv2.imshow('camera',img)
        
#        print(flag)
        if flag==10:
            flag=0
            cam.release()
            cv2.destroyAllWindows()
           

        if cv2.waitKey(1) == ord('Q'):
            break





        
        
            
    



#################################################################################################################
def window():
    root.destroy()



button1 = tk.Button(frame_alpr, text="Create Face Data", command=Create_database,width=15, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
button1.place(x=10, y=100)

button2 = tk.Button(frame_alpr, text="Train Face Data", command=Train_database, width=20, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
button2.place(x=10, y=160)

button3 = tk.Button(frame_alpr, text="Person Identification", command=Test_database, width=20, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
button3.place(x=10, y=220)

entry2=tk.Entry(frame_alpr,bd=2,width=7)
entry2.place(x=210, y=110)

exit = tk.Button(frame_alpr, text="Exit", command=window, width=20, height=1, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=10, y=340)



root.mainloop()
