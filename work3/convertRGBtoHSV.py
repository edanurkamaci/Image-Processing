import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


rgb=cv.imread('/home/edanurkamaci/pictures for image applications/4.2.06.tiff')
hsv=cv.cvtColor(rgb,cv.COLOR_BGR2HSV)

cv.imshow('RGB',rgb)
cv.imshow('HSV',hsv)

plt.subplot(1,1,1)
plt.imshow(hsv[:,:,0])
plt.title('H IMAGE')
plt.xticks([])
plt.yticks([])
plt.show()

plt.subplot(1,1,1)
plt.imshow(hsv[:,:,2])
plt.title('S IMAGE')
plt.xticks([])
plt.yticks([])
plt.show()

plt.subplot(1,1,1)
plt.imshow(hsv[:,:,2])
plt.title('V IMAGE')
plt.xticks([])
plt.yticks([])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()