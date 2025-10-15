import cv2
img = cv2.imread('assets/CR7.jpg')
cv2.imshow('image', img)
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Rotated', rotated)          
cv2.waitKey(0)
cv2.destroyAllWindows()