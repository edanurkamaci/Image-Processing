"""
1- Convert an image to black-white and save as (.name.)_bw
2- Convert the image to gray and save as (.name.)_gray
3- Look at (.name.)_bw and (.name.)_gray histograms' 
4- Interpret the histogram of (.name.)_gray. Make some changes onto the image
to understand why histogram is so important
5- Make (.name.)_gray image quantized as 2 bits. Interpret the change
6-Paint the area (including the middle pixel) that will enclose 
the 8-neighborhood of the middle pixel of the (.name.)_gray image in black on the image.
"""
#@author=Eda

import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

#missions 1,2,3

lena=cv.imread('/home/edanurkamaci/Image Processing/lena.png')
lena_gray=cv.cvtColor(lena,cv.COLOR_BGR2GRAY)
img=cv.imread('/home/edanurkamaci/Image Processing/lena.png',0)
(thresh, lena_bw) = cv.threshold(lena_gray, 127, 255, cv.THRESH_BINARY)

cv.imshow('LENA',lena)
cv.imshow('BLCK_WHT LENA',lena_bw)
cv.imshow('GRAY LENA',lena_gray)

"""
print(lena.dtype)

a1=lena+10
b=(a1+120)*2
print(np.amin(lena))
print(np.amax(lena))

#cv.imshow('A1',a1)
#cv.imshow('B',b)

b,g,r=cv.split(lena)

cv.imshow('LENA',lena)
cv.imshow('B',b)
cv.imshow('G',g)
cv.imshow('R',r)

plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])

hist_A=cv.calcHist([a1],[0],None,[256],[0,256])
hist_B=cv.calcHist([b],[0],None,[256],[0,256])

plt.plot(hist_A)
plt.plot(hist_B)
plt.show()
"""
#QUANTIZING LENA_GRAY

quantized_lenagray=lena//64*64+64//2
quant2=lena/pow(2,7) #unfourtanetly I thought wrong 
cv.imshow('quant',quantized_lenagray)
#cv.imshow('quant2',quant2)

#make histogram of gray lena 

plt.hist(lena_gray.ravel(),256,[0,256])
plt.show()

#hist_quant=cv.calcHist([quantized_lenagray],[0],None,[4],[0,4])
hist_bw=cv.calcHist([lena_bw],[0],None,[256],[0,256])
hist_gray=cv.calcHist([lena_gray],[0],None,[256],[0,256])
hist_lena=cv.calcHist([lena],[0],None,[256],[0,256])

plt.plot(hist_gray)
plt.plot(hist_bw)
#plt.plot(hist_quant)
plt.plot(hist_lena)

plt.show()

#print(lena)
#print(lena_gray)
#print(lena_bw)



#6

x=256
y=256

def paint_black(img,x,y):
    for i in range(-1,1+1):
        for j in range(-1,1+1):
            img[x+i,y+j]=0
    cv.imshow('after operations',img)
   
paint_black(img,x,y)
cv.imshow('Before Operations',lena_gray)

difference=lena_gray-img

cv.imshow('difference',difference)

cv.waitKey(0)
cv.destroyAllWindows()


"""
RESULTS:

1- When convert an image colored to gray or blac-white, the dimension also changes from 3D to 2D

"""