import numpy as np
import cv2
import time

img = cv2.imread('images/opencv-corner-detection-sample.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.intc(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,255,-1)
    
cv2.imshow('Corner',img)

while(True):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
    time.sleep(0.5)  # because its causing cpu utilization :( 
