import cv2
import time
from LiNet import LiNet

classobj = LiNet(netname='AlexNet')

cam = cv2.VideoCapture(0)
while True:
    img = cam.read()[1]
    item,_ = classobj.classify(img)
    img = cv2.putText(img, item, (100,100), cv2.FONT_HERSHEY_SIMPLEX ,  
                1, (255, 0, 0), 2, cv2.LINE_AA) 
    resized = cv2.resize(img, (300,200), interpolation = cv2.INTER_AREA)
    cv2.imshow("Window", resized)
    if cv2.waitKey(0)=='q':
        time.sleep(1)
        break
