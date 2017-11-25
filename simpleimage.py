import time
import cv2
import cv2.aruco as A
import numpy as np

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_250)

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
res = cv2.aruco.detectMarkers(gray,dictionary)
cv2.aruco.drawDetectedMarkers(gray,res[0],res[1])

cv2.imwrite('marker.png',gray)

cap.release()
cv2.destroyAllWindows()