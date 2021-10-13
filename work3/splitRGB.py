import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('/home/edanurkamaci/pictures for image applications/4.2.07.tiff')
(B, G, R) = cv.split(img)

zeros = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Red", cv.merge([zeros, zeros, R]))
cv.imshow("Green", cv.merge([zeros, G, zeros]))
cv.imshow("Blue", cv.merge([B, zeros, zeros]))



cv.waitKey(0)
cv.destroyAllWindows()