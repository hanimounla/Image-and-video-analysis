import cv2
import numpy as np

main = cv2.imread('images/opencv-template-matching-python-tutorial.jpg')
width = main.shape[1]
hight = main.shape[0]
img_rgb = cv2.resize(main, (int(width*0.5),int(hight*0.5)))

cv2.imshow('Main', img_rgb)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('images/opencv-template-for-matching.jpg',0)
width = template.shape[1]
hight = template.shape[0]
template = cv2.resize(template, (int(width*0.5),int(hight*0.5)))

w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.7
loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

cv2.imshow('Main', main)
cv2.imshow('Detected', img_rgb)
while(True):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()