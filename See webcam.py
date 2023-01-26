import numpy as np
import cv2
import mediapipe as mp
import time

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.flip(gray, 1)
    out.write(frame)

    #results = hands.process(gray)
    # print(results.multi_hand_landmarks)


   ## if results.multi_hand_landmarks:
     ##       mpDraw.draw_landmarks(gray, handLmk, mpHands.HAND_CONNECTIONS)



    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(gray, str(int(fps)), (10, 70,), cv2.FONT_HERSHEY_PLAIN, 3, (250, 0, 500), 3)



    cv2.imshow('frame', gray)




    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()


