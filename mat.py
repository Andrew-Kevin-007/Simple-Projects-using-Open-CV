import cv2
import numpy as np
blank = np.zeros((500,500,3), dtype='uint8')
blank[200:300, 300:400] = 255,0,0
cv2.imshow('Blank', blank)
cv2.waitKey(0)