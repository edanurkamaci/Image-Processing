import cv2 as cv
import numpy as np

img=cv.imread('/home/edanurkamaci/Image Processing/lena_noisy.png')

kernel1=np.array([[0,1,0],[1,-4,1],[0,1,0]])
kernel2=np.array([[1,1,1],[1,-8,1],[1,1,1]])
kernel3=np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
kernel4=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

output1=cv.filter2D(img,-1,kernel1)
output2=cv.filter2D(img,-1,kernel2)
output3=cv.filter2D(img,-1,kernel3)
output4=cv.filter2D(img,-1,kernel4)

zeropad1=cv.copyMakeBorder(output1,10,10,10,10,cv.BORDER_CONSTANT,value=0)
zeropad2=cv.copyMakeBorder(output2,10,10,10,10,cv.BORDER_CONSTANT,value=0)
zeropad3=cv.copyMakeBorder(output3,10,10,10,10,cv.BORDER_CONSTANT,value=0)
zeropad4=cv.copyMakeBorder(output4,10,10,10,10,cv.BORDER_CONSTANT,value=0)

cv.imshow('lena1',zeropad1)
cv.imshow('lena2',zeropad2)
cv.imshow('lena3',zeropad3)
cv.imshow('lena4',zeropad4)

cv.waitKey(0)
cv.destroyAllWindows()