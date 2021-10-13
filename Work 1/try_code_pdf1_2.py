#@author= Eda 

import cv2 as cv
from matplotlib import pyplot as plt
import numpy as py
import copy as c

lena=cv.imread('/home/edanurkamaci/Image Processing/lena.png')

gray_lena=cv.cvtColor(lena,cv.COLOR_BGR2GRAY)

cv.imshow('Lena image - gray scale',gray_lena)

gray_lena2=c.copy(gray_lena)
gray_lena2[40:100,80:400]=0
cv.imshow('Gray new Lena',gray_lena2)

plt.imshow(gray_lena2)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()

"""
Question:

1- Why are images that was readed befor i use plt lib totally black?
2- what does Pyplot.imshow(..)->pyplot.show() do?

Answers:

1- ?
2- The imshow() function in pyplot module of matplotlib library is used to 
   display data as an image; i.e. on a 2D regular raster.

"""