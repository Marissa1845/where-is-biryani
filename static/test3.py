import cv2
import numpy as np
import time

def find(level):
    if level==1:
        img_rgb = cv2.imread('biryani-full.jpg')
        img_gray = cv2.imread('biryani-full.jpg',0)
        template = cv2.imread('biryani-sample.jpg',0)
    elif level==2:
        img_rgb = cv2.imread('birbir2.png')
        img_gray = cv2.imread('birbir2.png',0)
        template = cv2.imread('b2.jpg',0)
    elif level==3:
        img_rgb = cv2.imread('birbir3.png')
        img_gray = cv2.imread('birbir3.png',0)
        template = cv2.imread('b3.png',0)        
    # saves the width and height of the template into 'w' and 'h'
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.6
    # finding the values where it exceeds the threshold
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        #draw rectangle on places where it exceeds threshold
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
    cv2.imwrite('found_biryani1.png',img_rgb)


find(1)
#find (2)
#find (3)
