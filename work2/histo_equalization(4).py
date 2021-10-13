import cv2 as cv
import numpy as np
from matplotlib import pyplot as py
import copy as c

img=cv.imread('/home/edanurkamaci/Image Processing/trees.bmp',0)

cv.imshow('FIRST',img)

histo=np.zeros((256,),dtype=np.float16)
height,width=img.shape
MN=1.0/img.size

def compute(img,histo,size1,size2):
    for i in range(size1):
        for j in range(size2):
            num=img[i][j]
            histo[num]=histo[num]+1

compute(img,histo,img.shape[0],img.shape[1])
output=c.copy(histo)
val=0.0

for i in range(256):
    val+=histo[i]*MN
    output[i]=round(255*val)        

py.hist(img.ravel(),256,[0,256])
py.show()

for i in range(height):
    for j in range(width):
        a=img[i][j]
        img[i][j]=output[a]

cv.imshow('SECOND',img)

py.hist(img.ravel(),256,[0,256])
py.show()

cv.waitKey(0)
cv.destroyAllWindows()

"""
RESULTS:

1- I dont understand where I was wrong. I was successful thanks to my friend's algorithm. 1 or 2 things
  were different. It could be because of the way I create zero list or matrix, but our algortihm's results were
  different too. I am pretty sure that my algorithm was also true. 

  TRY TO UNDERSTAND WHAT THE FUCK WAS WRONG WITH YOUR ALGORITHM ANOTHER TIME!!!!

2- After equalization operation, my histogram be ploted wrong and also last histogram too I guess.
   these little mistakes drive me crazy
   
"""