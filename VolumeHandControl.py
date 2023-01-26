import cv2
import time
import numpy as np

import math

import HandTrackingModule as htm


from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

###############
wCam, hCam = 640, 480
##############

detector = htm.handDetector(detectionCon=0.7)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0
cTime = 0




def Map(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min



devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

volume = cast(interface, POINTER(IAudioEndpointVolume))




while True:
    sucess, img = cap.read()
    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList)!=0:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2

        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)

        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)

        length = math.hypot((x2-x1), (y2-y1))

        ##########################################
        #Adjust:
        #00 - 100 normal
        ## 100 - 00 reverse

        length = Map(length, 25, 110, 00, 100)
        #########################################

        length = np.clip(length, 00, 100)

        if length==0:
            cv2.circle(img, (cx, cy), 10, (0, 250, 0), cv2.FILLED)


        # volume.GetMute()
        # volume.GetMasterVolumeLevel()

        volume.SetMasterVolumeLevel(Map(length, 00, 100, -47.25, 00), None)



        cv2.putText(img, "volume: " + str(int(length)) + "%", (20, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
        cv2.rectangle(img, (50,150), (85, 400), (255, 0, 0), 3)
        cv2.rectangle(img, (50 ,int(np.interp(length, [00,100], [400, 150]))), (85, 400), (255, 0, 0), cv2.FILLED)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, "FPS: " + str(int(fps)), (20, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)