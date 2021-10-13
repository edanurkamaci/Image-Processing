import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img= cv.imread('/home/edanurkamaci/Image Processing/castle.png',0)
#cv.imshow('IMG',img)
size,size2=img.shape
histo=np.zeros((256,))
print(img.dtype)
#Compute histogram of an image yourself

def compute(img,histo,size,size2):
     for i in range(size):
        for j in range(size2):
            num=img[i][j]
            histo[num]+=1

compute(img,histo,size,size2)

#histo_=cv.calcHist([img],[0],None,[256],[0,256])
plt.hist(img.ravel(),256,[0,256])
plt.plot(histo)
#plt.plot(histo_)

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()