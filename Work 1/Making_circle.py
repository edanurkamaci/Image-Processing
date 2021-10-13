#@author= Eda

import cv2 as cv
import numpy as np

black=np.zeros((256,256,3),np.uint8)
bw_circle=cv.circle(black,(128,128),80,(255,255,255),-1)

imgg=np.zeros((256,256,3),np.uint8)

def create_gray(img,size):
    for i in range(size):
        for j in range(size):
            img[i,j]=j
    cv.imshow('1',img)

create_gray(imgg,256)

gray_circ=imgg/bw_circle

cv.imshow('1',imgg)
cv.imshow('2',gray_circ)
cv.imshow('CIRCLE',bw_circle)

cv.waitKey(0)
cv.destroyAllWindows()