import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import copy as c


"""""
def filter2d(src, kernel):

    m, n = kernel.shape

    d = int((m-1)/2)
    h, w = src.shape[0], src.shape[1]

    dst = np.zeros((h, w))

    for y in range(d, h - d):
        for x in range(d, w - d):
            dst[y][x] = np.sum(src[y-d:y+d+1, x-d:x+d+1]*kernel)

    return dst
"""""
lena=cv.imread('/home/edanurkamaci/Image Processing/lena.png',0)

kernel1=np.array([[0,1,0],[1,-4,1],[0,1,0]])
kernel2=np.array([[1,1,1],[1,-8,1],[1,1,1]])
kernel3=np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
kernel4=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

dst1= cv.filter2D(lena, cv.CV_64F, kernel1)
dst2=  cv.filter2D(lena, cv.CV_64F, kernel2)
dst3= cv.filter2D(lena, cv.CV_64F, kernel3)
dst4=  cv.filter2D(lena, cv.CV_64F, kernel4)

cv.imshow('Upper-Left',dst1)
cv.imshow('Bottom-Left',dst2)
cv.imshow('Upper-Right',dst3)
cv.imshow('Bottom-Right',dst4)

cv.waitKey(0)
cv.destroyAllWindows()