import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt



img=cv.imread('/home/edanurkamaci/pictures for image applications/4.2.07.tiff')

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

f=plt.figure('ORIGINAL') 
plt.imshow(img)
plt.show(f)

pixel_vals = img.reshape((-1,3))
 
# Convert to float type
pixel_vals = np.float32(pixel_vals)

criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.85)
 
# then perform k-means clustering wit h number of clusters defined as 3
#also random centres are initially choosed for k-means clustering
k = 8
retval, labels, centers = cv.kmeans(pixel_vals, k, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)
 
# convert data into 8-bit values
centers = np.uint8(centers)
segmented_data = centers[labels.flatten()]
 
# reshape data into the original image dimensions
segmented_image = segmented_data.reshape((img.shape))
 
g=plt.figure('When k=4') 
plt.imshow(segmented_image)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()