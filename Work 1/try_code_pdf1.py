#@author= Eda 
"""
1- Reading a image
2- Convert the image to black
3- Print both max and minimum of both normal lena and black lena
4- Print both shape and size of both normal lena and black lena
5- Show the user colorful lena and black lena
6- Resize the colorful lena
7- Show the lena unresized to user by printing
8- Show user new lena resized by printing

"""

import cv2 as cv 
import numpy as py

img= cv.imread('/home/edanurkamaci/Image Processing/lena.png')
black_img=cv.imread('/home/edanurkamaci/Image Processing/lena.png',0)

height=img.shape[0]
width=img.shape[1]

print("Max size of lena: ",py.max(img))
print("Minimum size of lena: ",py.min(img))
print("Max size of black lena: ",py.max(black_img))
print("Minimum size of black lena: ",py.min(black_img))

print("Height of the normal image: ",height)
print("Width of the normal image: ",width)
print("Shape of normal image: ",img.shape)
print("Size of normal image: ",img.size)
print("Size of black image: ",black_img.size)
print("Shape of black image: ",black_img.shape)

cv.imshow('Lena',img)
cv.imshow('Black Lena',black_img)

#resize image:

height2=int(img.shape[0]*1.5)
width2=int(img.shape[1]*0.8)

dim=(height2,width2)

resized=cv.resize(img,dim,interpolation=cv.INTER_AREA)

cv.imshow('image resized',resized)

#resized again:

height3=int(img.shape[0]*0.4)        
width3=int(img.shape[1]*0.4)

dim2=(height3,width3)

resized2=cv.resize(img,dim2,interpolation=cv.INTER_AREA)

cv.imshow('image resized 2',resized2)

cv.waitKey(0)

"""
Results: 

I can not understand that when i resize the image, sizes of image are revers of 
each others according to rate values i entered

I guess altough we use resize function multiple times, it impressive original image each time
no matter it is first resized or whatever

The image Lena that is colorful is 3D array, but when we convert it to black, its array dimension 
changes either. I mean 2D dimension.  
"""