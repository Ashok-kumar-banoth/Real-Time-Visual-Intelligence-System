import cv2
from PIL import Image

from util import get_limits

yellow = [0, 255, 255]#yellow in BGR colorspace

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read() #reads frames

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #this will convert from original to hsv image
    
    loweLimit, upperLimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage, loweLimit, upperLimit)# gives where the pixels crresponds to the color are present
    mask_ = Image.fromarray(mask)
    bbox= mask_.getbbox()
    print(bbox)

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2),(0,255,0),5)
    cv2.imshow("mask", mask)
    cv2.imshow('frame', frame)#visualise
    #blue, green and red
    #hue , saturation and value

    if cv2.waitKey(2) & 0xFF ==ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
