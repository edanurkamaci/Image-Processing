import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import copy as c

img1=cv.imread('/home/edanurkamaci/Downloads/image00392.jpg',0)
cv.imshow('FIRST',img1)

hist=np.zeros(256,dtype=int)
size1=img1.shape[1]
size2=img1.shape[0]
img1=255-img1

def compute(img,histo,size,size2):
     for i in range(size):
        for j in range(size2):
            num=img[i][j]
            histo[num]+=1

compute(img1,hist,size2,size1)

first_var,second_var=0,0
for j in range(256):
    p1,p2,m1,m2=0,0,0,0
    for i in range(j):
            p1+=hist[i]/img1.size
            m1+=(i*(hist[i]/img1.size))
    for i in range(j,256):
        m2+=(i*(hist[i]/img1.size))
    p2=1-p1
    if(p1!=0 and p2!=0):
        m1*=1/p1
        m2*=1/p2
        Mg=(p1*m1)+(p2*m2)
        second_var=pow((p1*(Mg-m1)),2)/(p1*p2)
        #print(second_var,first_var, j)
        if(second_var>first_var):
            k=j
            p1_,p2_,m1_,m2_,Mg_=p1,p2,m1,m2,Mg
            first_var=second_var    

for i in range(size2):
   for j in range(size1):
       if(img1[i,j]<k):
           img1[i,j]=0
       else:
           img1[i,j]=255   
    
print('P1: ',p1_,'M1: ',m1_,'\nP2: ',p2_,'M2: ',m2_,'\nMg: ',Mg_,'\nBetween Variance: ',first_var,'k: ',k)

cv.imshow('SECOND',img1)


cv.waitKey(0)
cv.destroyAllWindows()