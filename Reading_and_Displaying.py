import cv2 #importing the module

#OpenCv reads an image as a matrix

"""Reading and Displaying"""

img=cv2.imread("flower.jpg",1) # reading a Coloured Image
#img_1=cv2.imread("flower.jpg",0)Gray scale
cv2.imshow("flower",img)

cv2.waitKey(0)#Wait until the user presses a key
#cv2.waitKey(2000)#Wait until the user presses a key
cv2.destroyAllWindows()#Closes the window based on waitKey parameter
