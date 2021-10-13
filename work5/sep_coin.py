import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import copy as c

img=cv.imread('/home/edanurkamaci/Downloads/image00392.jpg',0)
size1,size2=img.shape[0],img.shape[1]
img=255-img

cv.imshow('normal',img)
T=80

for i in range(size1):
    for j in range(size2):
        if(img[i,j]<T):
            img[i,j]=0
        else:
            img[i,j]=255

img2=c.copy(img)

cv.imshow('first',img)
flag=0

for m in range(2):
    for i in range(1,size1-1):
        for j in range(1,size2-1):
            for a in range (-1,2):
                for b in range(-1,2):
                    if(img[i+a,j+b]==255):
                        img2[i,j]=255
                        flag=1
                        break
                if(flag==1):
                   break
            flag=0
    img=c.copy(img2)

cv.imshow('second',img2)

for m in range(5):
    for i in range(1,size1-1):
        for j in range(1,size2-1):
            for a in range (-2,3):
                for b in range(-2,3):        
                    if(img[i+a,j+b]==0):
                        img2[i,j]=0
                        flag=1
                        break                   
                if(flag==1):
                   break
            flag=0
    img=c.copy(img2)

cv.imshow('Third',img2)

cv.waitKey(0)
cv.destroyAllWindows()