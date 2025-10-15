import cv2
img = cv2.imread('#imgpath')
cv2.imshow('CR7', img)
flip_h = cv2.flip(img, 1)
flip_v = cv2.flip(img, 0)   
cv2.imshow('Flip Horizontal', flip_h)
cv2.imshow('Flip Vertical', flip_v)
cv2.waitKey(0)

cv2.destroyAllWindows()
