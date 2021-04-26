import cv2
img=cv2.imread("three.jpg",0)
print(img)
print(img.shape)
print(type(img))
cv2.imshow("WIE",img)
cv2.waitKey(0)
cv2.destroyAllWindows()