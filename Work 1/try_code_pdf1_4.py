import cv2 as cv
import numpy as np
from matplotlib import pyplot as py
import copy as c

A=cv.imread('/home/edanurkamaci/Image Processing/lena.png',0)

print(A.dtype)

a1=A[234,456]
b=a1+150

print('a1: {}  |  b: {}'.format(a1,b))

a2=A[234,456]
b2=a2+150

print('a2: {}  |  b2: {}'.format(a2,b2))
print('----------------------')


print('size: ',A.size)
print('shape: ',A.shape)
print(A.dtype)

B=c.copy(A)

for i in range(512):
    for j in range(512):
        B[i,j]+=100
        
cv.imshow('first',A)
cv.imshow('second',B)

cv.waitKey(0)
cv.destroyAllWindows()

#TRY TO SCAN IMAGES ON AXES !!!!!!