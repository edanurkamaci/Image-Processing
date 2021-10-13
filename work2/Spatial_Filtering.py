# @Author: Eda
"""""
1- Applying zero-padding make mask filter on lena_noisy pic.

"""""
import cv2 as cv
import numpy as np
from matplotlib import pyplot as py
import copy as c

img=cv.imread('/home/edanurkamaci/Image Processing/lena_noisy.png',0)
cv.imshow('LENA',img)
#kernel2=[[0,1,0],[1,-4,1],[0,1,0]]
kernel2=[[1,1,1],[1,-8,1],[1,1,1]]
#kernel2=[[0,-1,0],[-1,4,-1],[0,-1,0]]
#kernel=[[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
kernel=(np.ones((3,3),dtype=np.float32))/16
#kernel=[[1,2,1],[2,4,2],[1,2,1]]
k=3//2
new =np.zeros((514,514),dtype=np.uint8)
img2=c.copy(img)

for i in range(512):
    for j in range(512):
        new[i+k][j+k]=img2[i][j]

sum=0.0

for i in range(k,512+k*2-k,k):
    for j in range(k,512+k*2-k):
        for m in range(3):
            for l in range(3):
                sum+=(new[i+m-k][j+l-k]*kernel[m][l])
        img2[i-k][j-k]=sum/(9/16)
        sum=0.0

img2=img-img2

for i in range(k,512+k*2-k):
    for j in range(k,512+k*2-k):
        for m in range(3):
            for l in range(3):
                sum+=(new[i+m-k][j+l-k]*kernel2[m][l])
        img2[i-k][j-k]=sum
        sum=0.0

cv.imshow('LENA 2',img2)

cv.waitKey(0)
cv.destroyAllWindows()
