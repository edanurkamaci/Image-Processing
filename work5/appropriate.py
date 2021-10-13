import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import copy as c

img=cv.imread('/home/edanurkamaci/Downloads/31InWKMUyRL._SX258_BO1,204,203,200_.jpg',0)

size1,size2=img.shape[0],img.shape[1]
img=255-img
b=[[0,1,0],[1,1,1],[0,1,0]]
T=111
flag=0

for i in range(size1):
    for j in range(size2):
        if(img[i,j]<T):
            img[i,j]=0
        else:
            img[i,j]=255
cv.imshow('FIRST',img)
img2=c.copy(img)
img3=c.copy(img)

for m in range(1):
    for i in range(1,size1-1):
        for j in range(1,size1-1):
            for a in range (-1,2):
                for b in range(-1,2):
                    if(img[i+a,j+b]==0):
                        img2[i,j]=0
                        flag=1
                        break
                if(flag==1):
                   break
            flag=0
    img=c.copy(img2)

img2=img3-img2
cv.imshow('SECOND',img2)

cv.waitKey(0)
cv.destroyAllWindows()