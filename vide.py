import cv2
cap = cv2.VideoCapture('assets/bg.mp4')
while True:
    success,frame = cap.read()
    if not success:
        break
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()