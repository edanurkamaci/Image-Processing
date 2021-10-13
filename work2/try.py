import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import copy as c

img=cv.imread('/home/edanurkamaci/pictures for image applications/7.2.01.tiff',0)
img2=c.copy(img)
x=img.shape[0]
y=img.shape[1]

for i in range(x):
    for j in range(y):
        img2[i,j]=30*pow(img2[i,j],0.4)

cv.imshow('LENA-1',img)
cv.imshow('LENA-2',img2)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()