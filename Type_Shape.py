import cv2 #importing the module

#OpenCv reads an image as a matrix

""" Image Characteristics"""

img=cv2.imread("flower.jpg",1)    # reading a Coloured Image

print("Image is in the form a 3D matrix")
print(img)#3D array

print("The size of the image is : ")
print(img.shape)

print("The type of the image is : ")
print(type(img))

cv2.waitKey(0)#Wait until the user presses a key
#cv2.waitKey(2000)#Wait until the user presses a key
cv2.destroyAllWindows()#Closes the window based on waitKey parameter