import cv2
import numpy as np
import time

def find1():
    img_rgb = cv2.imread('biryani-full.jpg')
    img_gray = cv2.imread('biryani-full.jpg',0)
    #img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('biryani-sample.jpg',0)
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
    cv2.destroyAllWindows()


def find2():
    img_rgb1 = cv2.imread('birbir2.png')
    img_gray1 = cv2.imread('birbir2.png',0)
    #img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template1 = cv2.imread('b2.jpg',0)
    # saves the width and height of the template into 'w' and 'h'
    w, h = template1.shape[::-1]
    res = cv2.matchTemplate(img_gray1,template1,cv2.TM_CCOEFF_NORMED)
    threshold = 0.6
    # finding the values where it exceeds the threshold
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        #draw rectangle on places where it exceeds threshold
        cv2.rectangle(img_rgb1, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
    cv2.imwrite('found_biryani2.png',img_rgb1)
    cv2.destroyAllWindows()


def find3():
    img_rgb2 = cv2.imread('birbir3.png')
    img_gray2 = cv2.imread('birbir3.png',0)
    #img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template2 = cv2.imread('b3.png',0)
    # saves the width and height of the template into 'w' and 'h'
    w, h = template2.shape[::-1]
    res = cv2.matchTemplate(img_gray2,template2,cv2.TM_CCOEFF_NORMED)
    threshold = 0.6
    # finding the values where it exceeds the threshold
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        #draw rectangle on places where it exceeds threshold
        cv2.rectangle(img_rgb2, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
    cv2.imwrite('found_biryani3.png',img_rgb2 )


    
find1()
find2()
find3()