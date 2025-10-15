import cv2
img = cv2.imread('assets/CR7.jpg')
blur = cv2.GaussianBlur(img, (7,7), cv2.BORDER_DEFAULT)
cv2.imshow('Blurred', blur)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
