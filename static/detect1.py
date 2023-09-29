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
    elif level==4:
        img_rgb = cv2.imread('birbir4.png')
        img_gray = cv2.imread('birbir4.png',0)
        template = cv2.imread('b4.png',0)        
    # saves the width and height of the template into 'w' and 'h'
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.6
    # finding the values where it exceeds the threshold
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        #draw rectangle on places where it exceeds threshold
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
    cv2.imwrite('found_biryani'+str(level)+'.png',img_rgb)


def Time():
    tic = time.perf_counter()
    find(1)
    toc = time.perf_counter()
    time1 = toc-tic
    find(2)
    tic = time.perf_counter()
    time2 = tic - toc
    find(3)
    toc = time.perf_counter()
    time3 = toc - tic
    find(4)
    tic = time.perf_counter()
    time4 = tic-toc
    return [time1, time2, time3, time4]