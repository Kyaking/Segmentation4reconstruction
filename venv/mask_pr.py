import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('/home/kyaking/downloads/pic/rose/DSC_3430.jpg')

img2 = cv.imread('/home/kyaking/downloads/pic/rose/mask.png')
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
# mask = cv.resize(mask, img.shape[0::1])
print(mask.dtype)
img_mask = cv.bitwise_and(img,img,mask = mask)
cv.imshow('666',img_mask)
cv.imwrite('/home/kyaking/downloads/pic/rose/DSC_3430_mask2.jpg',img_mask)
cv.waitKey(0)
cv.destroyAllWindows()