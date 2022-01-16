import posemodule as pm
import time
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import cvzone
import requests

blynk_auth = '' # wenter your blynk auth
cap2 = cv2.VideoCapture(1)
cap2.set(3, 1280)
cap2.set(4, 720)
detector2 = HandDetector(detectionCon=0.8)

def get_frame():

    success, img = cap2.read()
    img = cv2.flip(img, 1)
    hands, img = detector2.findHands(img, flipType=False)
    img, bbox = cvzone.putTextRect(img, "   Welcome VR Automation  ", [350, 150], 2, 2, offset=50, border=5)
    img, bbox1 = cvzone.putTextRect(img, 'Relay 1 ON', [350, 300], 2, 2, offset=50, border=5)
    img, bbox2 = cvzone.putTextRect(img, 'Relay 1 OFF', [680, 300], 2, 2, offset=50, border=5)

    img, bbox3 = cvzone.putTextRect(img, 'Relay 2 ON', [350, 450], 2, 2, offset=50, border=5)
    img, bbox4 = cvzone.putTextRect(img, 'Relay 2 OFF', [680, 450], 2, 2, offset=50, border=5)

    img, bbox5 = cvzone.putTextRect(img, 'Relay 3 ON', [350, 600], 2, 2, offset=50, border=5)
    img, bbox6 = cvzone.putTextRect(img, 'Relay 3 OFF', [680, 600], 2, 2, offset=50, border=5)
    if hands:
        lmList = hands[0]['lmList']
        cursor = lmList[8]
        length, info = detector2.findDistance(lmList[8], lmList[12])       
        if length < 35:
            bboxs = [bbox, bbox1, bbox2 , bbox3 , bbox4 , bbox5 , bbox6]
            for x, bbox in enumerate(bboxs):
                x1, y1, x2, y2 = bbox
                if x1 < cursor[0] < x2 and y1 < cursor[1] < y2:
                    userAns = x + 1
                    print(userAns)
                    print('this is length of bb boxes '+str(len(bboxs)))
                    # for i in range(len(bboxs)+1):
                    # cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), cv2.FILLED)
                    if userAns == 0:
                        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), cv2.FILLED)
                        print('correct completed')
                        return userAns
                    if userAns == 1:
                        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), cv2.FILLED)
                        
                                
                    if userAns == 2:
                        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), cv2.FILLED)
                        print('correct completed')
                        try:
                            requests.get(f'http://188.166.206.43/{blynk_auth}/update/V1?value=0')
                            print('success traffic light changed')
                            
                        except: print('error sending the data')
                        time.sleep(0.1)
                    if userAns == 3:
                        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), cv2.FILLED)
                        print('correct completed')
                        try:
                            requests.get(f'http://188.166.206.43/{blynk_auth}/update/V1?value=1')
                            print('success traffic light changed')
                            
                        except: print('error sending the data')
                        time.sleep(0.1)
                    if userAns == 4:    
                        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), cv2.FILLED)
                        print('correct completed')
                        try:
                            requests.get(f'http://188.166.206.43/{blynk_auth}/update/V2?value=0')
                            print('success traffic light changed')
                            
                        except: print('error sending the data')
                        time.sleep(0.1)
                    if userAns == 5:    
                        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), cv2.FILLED)
                        print('correct completed')
                        try:
                            requests.get(f'http://188.166.206.43/{blynk_auth}/update/V2?value=1')
                            print('success traffic light changed')
                            
                        except: print('error sending the data')
                        time.sleep(0.1)
                    if userAns == 6:    
                        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), cv2.FILLED)
                        print('correct completed')
                        try:
                            requests.get(f'http://188.166.206.43/{blynk_auth}/update/V3?value=0')
                            print('success traffic light changed')
                            
                        except: print('error sending the data')
                        time.sleep(0.1)
                    if userAns == 7:    
                        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), cv2.FILLED)
                        print('correct completed')
                        try:
                            requests.get(f'http://188.166.206.43/{blynk_auth}/update/V3?value=1')
                            print('success traffic light changed')
                            
                        except: print('error sending the data')
                        time.sleep(0.1)
                    if userAns == 8:    
                        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), cv2.FILLED)
                        print('correct completed')
                    # if userAns == 5:    
                    #     cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), cv2.FILLED)
                    #     print('correct completed')

                        return userAns
                        
    cv2.imshow("Img", img)
    cv2.waitKey(1)


while True:
        nm = get_frame()
        print(nm)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap2.release()
            cv2.destroyAllWindows()
            print('completed')
            break
