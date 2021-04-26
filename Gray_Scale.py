import cv2 #importing the module

#OpenCv reads an image as a matrix

"""Reading and Displaying"""

img1=cv2.imread("build.jpg",0) # reading a Grayscale Image
#img_1=cv2.imread("flower.jpg",0)Gray scale
cv2.imshow("New York",img1)

cv2.waitKey(0)#Wait until the user presses a key

cv2.destroyAllWindows()#Closes the window based on waitKey parameter
