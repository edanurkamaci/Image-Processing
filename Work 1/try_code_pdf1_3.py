import cv2 as cv
import numpy as np
import copy

img=cv.imread('/home/edanurkamaci/Image Processing/lena.png')

size=img.size
height,width,z=img.shape

print(size)
print(height,width,z)

max=np.max(img)
min=np.min(img)
print('Max value: {} | Min value: {}'.format(max,min))

#print(img[:,:,:])

img2=copy.copy(img)
img2[40:100,80:400]=0

cv.imshow('LENA',img)
cv.imshow('LENA-2',img2)


cv.waitKey(0)
cv.destroyAllWindows()