import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('/home/edanurkamaci/pictures for image applications/4.1.08.tiff',0)

cv.imshow('FIRST',img)

T=127
sum1,m1=0,0
sum2,m2=0,0
hist=np.zeros(256,dtype=int)
size1=img.shape[1]
size2=img.shape[0]

def compute(img,histo,size,size2):
     for i in range(size):
        for j in range(size2):
            num=img[i][j]
            histo[num]+=1

compute(img,hist,size2,size1)

while(1):
    for i in range(int(T)):
        m1+=hist[i]*i
        sum1+=hist[i]
    for i in range(int(T),256):
        m2+=hist[i]*(i)
        sum2+=hist[i]
    m1/=sum1
    m2/=sum2
    T2=(m1+m2)/2

    if(abs(T-T2)<2):
        break
    else:
        T=T2
        sum1,sum2,m1,m2=0,0,0,0
print('Thresholding value: ',int(T2))
plt.hist(img.ravel(),256,[0,256])

for i in range(size2):
    for j in range(size1):
        if(img[i,j]<T2):
            img[i,j]=0
        else:
            img[i,j]=255

cv.imshow('SECOND',img)        

plt.hist(img.ravel(),256,[0,256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()