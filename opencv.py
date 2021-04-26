#face detection
import cv2
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
img=cv2.imread("C:\\Users\\Pratya Chandrayan\\Downloads\\faces.jpeg")
faces=face_cascade.detectMultiScale(img,ScaleFactor=1.05,minNeighbors=5);
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,256,0),3)
    cv2.imshow("face detection",img)
cv2.waitKey(0)
#text to an image
import cv2
path = "C:\\Users\\Pratya Chandrayan\\Downloads\\w.jpg"
img = cv2.imread(path)
resized=cv2.resize(img,(600,600))
font = cv2.FONT_HERSHEY_SIMPLEX   
cv2.putText(resized,'Women in Engineering',(200,200), font, 1 ,(365,365,365),2 )
cv2.imshow("img",resized)
cv2.waitKey(0)  
cv2.destroyAllWindows()
#video capturing
import cv2    
video=cv2.VideoCapture(0)      
a=1    
while True: 
    a=a+1
    check,frame=video.read()
    print(frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  
    cv2.imshow("capturing",frame)  
    key=cv2.waitKey(1)   
    if key==ord('q'):   
        break            
print(a) 
video.release() 
cv2.destroyAllWindows()
