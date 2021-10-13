import cv2 as cv
import numpy as np

img=np.ones((200,200),dtype=np.uint8)

for i in range(-100,100):
    for j in range(-100,100):
        if((i<-80 or i>80) and (j<-80 or j>80)):
            img[i+100,j+100]=0
        if( (i<-60 or i>60) and (j<-60 or j>60) ):
            img[i+100,j+100]=64
        if( (i<-40 or i>40) and (j<-40 or j>40)):
            img[i+100,j+100]=128
        if( (i<-20 or i>20) and (j<-20 or j>20)):
            img[i+100,j+100]=192
        if((i<0 or i>0) and (j<0 or j>0)):
            img[i+100,j+100]=255   
 

cv.imshow('1',img)

cv.waitKey(0)
cv.destroyAllWindows()