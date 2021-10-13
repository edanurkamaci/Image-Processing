import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import copy as c

#Mission-1: Convert lena to black one and gray one
lena=cv.imread('/home/edanurkamaci/Image Processing/lena.png')
lena_bw=np.zeros((512,512),dtype=np.uint8)
lena_gray=cv.cvtColor(lena,cv.COLOR_BGR2GRAY)

for i in range(512):
    for j in range(512):
        if(lena[i,j,0]<255/2): 
            lena_bw[i,j]=0
        else:
            lena_bw[i,j]=255

cv.imshow('LENA-BLACK',lena_bw)
cv.imshow('LENA-GRAY',lena_gray)
cv.imshow('LENA',lena)
""""
plt.hist(lena.ravel(),256,[0,256])
plt.hist(lena_gray.ravel(),256,[0,256])

plt.show()

#QUANTİZE 8-BIT IMAGE TO 2-BIT IMAGE

lena2Bit=c.copy(lena_gray)
interval=pow(2,8)/pow(2,2)

for i in range(512):
    for j in range(512):
        if(lena2Bit[i,j]>=0 and lena2Bit[i,j]<interval):
            lena2Bit[i,j]=(interval-1)/2
        elif(lena2Bit[i,j]>=interval and lena2Bit[i,j]<interval*2):
            lena2Bit[i,j]=(interval+(interval*2)-1)/2
        elif(lena2Bit[i,j]>=interval*2 and lena2Bit[i,j]<interval*3):
            lena2Bit[i,j]=(interval*2+(interval*3)-1)/2
        elif(lena2Bit[i,j]>=interval*3 and lena2Bit[i,j]<interval*4):
            lena2Bit[i,j]=(interval*3+(interval*4)-1)/2

cv.imshow('Lena-gray 8-bit',lena_gray)
cv.imshow('Lena-gray 2-bit',lena2Bit)

#paint black middle of the image

x=256
y=256
for i in range(-1,1+1):
        for j in range(-1,1+1):
            lena_gray[x+i,y+j]=0
cv.imshow('LENA_GRAY with black point',lena_gray)
 """
cv.waitKey(0)
cv.destroyAllWindows()