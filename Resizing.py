import cv2 #importing the module

#OpenCv reads an image as a matrix

""" RESIZING """

img=cv2.imread("flower.jpg",1) # reading a Coloured Image
#img_1=cv2.imread("flower.jpg",0)Gray scale
resize=cv2.resize(img,(600,600))
cv2.imshow("flower",resize)#opens a window to display image"""
cv2.waitKey(0)#Wait until the user presses a key
cv2.destroyAllWindows()#Closes the window based on waitKey parameter

