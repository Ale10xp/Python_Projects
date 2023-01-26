import cv2
import mediapipe as mp
import time

import HandTrackingModule as htm

import math
import numpy as np


import pyautogui as pg

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
detector = htm.handDetector()
distance = 0


def Map(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min



while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img, draw=True)


    lmList = detector.findPosition(img, draw=False)
    
    if len(lmList) != 0:

        x1 = lmList[4][1];
        x2 = lmList[12][1]

        y1 = lmList[4][2]
        y2= lmList[12][2]
        
        distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2))


        #print(lmList[4])

        
        cv2.line(img, (lmList[4][1], lmList[4][2]),  (lmList[12][1], lmList[12][2]), (200, 0, 200),2)
        
        cv2.circle(img, (lmList[8][1], lmList[8][2]), 4, (255, 0, 255), cv2.FILLED)

        
        
        #pg.moveTo(int(Map(lmList[8][1], -img.shape[0]/2, img.shape[0]/2, 0, 1200)),
         #        int(Map(lmList[8][2], -img.shape[1]/2, img.shape[1]/2, 0, 1200)))


        pg.moveTo(int(lmList[8][1]*3),int(lmList[8][2]*3))
        
        
        #cv2.line(img, (lmList[4][1], lmList[4][2]), (lmList[12][1], lmList[12][2]), (200, 0, 200), 2)
        #cv2.line(img, (lmList[4][1], lmList[4][2]), (lmList[16][1], lmList[16][2]), (200, 0, 200), 2)
        #cv2.line(img, (lmList[4][1], lmList[4][2]), (lmList[20][1], lmList[20][2]), (200, 0, 200), 2)


    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)
    mapped_distance = (int(Map(distance, 20,100, 00, 100)))
    
    clipped_distance = np.clip(mapped_distance, 0,100)

    if detector.findPosition(img, draw=False):
        if clipped_distance == 0:
            cv2.circle(img, (lmList[8][1], lmList[8][2]), 16, (255, 255, 0), cv2.FILLED)
            pg.click()
    
    cv2.putText(img, "distance: " + str(clipped_distance), (70, 450), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 2)                

    cv2.imshow("Image", img)
    cv2.waitKey(1)
