import cv2
import numpy as np
from pyzbar.pyzbar import decode

from datetime import datetime

def time():
    now=datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time
    
def interpret(image):
    blue_img = cv2.cvtColor(image,0)
    barcode = decode(blue_img)
    
    for picture in barcode:
        points = picture.polygon
        (x,y,w,h) = picture.rect
        asd = np.array(points, np.int32)
        asd = asd.reshape((-1,1,2))
        cv2.polylines(image,[asd],True,(37, 150, 190),3) 
        
        Data = picture.data.decode("utf-8")
        
        
        with open("me.txt", "w") as txt:
            txt.write(Data)
            txt.write(time())
            
Tle = cv2.VideoCapture(0)
while True:
    ret, frame = Tle.read()
    interpret(frame)
    cv2.imshow('Image', frame)
    code = cv2.waitKey(10)
    if code == ord('q'):
        break
