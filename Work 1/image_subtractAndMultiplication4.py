import cv2 as cv

img=cv.imread('/home/edanurkamaci/pictures for image applications/lena_color_512.tif')
img2=cv.imread('/home/edanurkamaci/pictures for image applications/lena_gray_512.tif')
multip_img=abs(img*img2)
sub_img=abs(img-img2)

cv.imshow('colorful lena', img)
cv.imshow('gray lena', img2)
cv.imshow('LENA DOT', multip_img)
cv.imshow('LENA SUB', sub_img)

cv.waitKey(0)
cv.destroyAllWindows()