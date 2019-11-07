import numpy as np
import cv2
from matplotlib import pyplot as plt
img1 = cv2.imread('/home/kyaking/downloads/pic/rose/DSC_3430.jpg')
# img1 = cv2.imread('/home/kyaking/downloads/pic/papri_rota/IMG_6796.JPG',0)# queryImage
# print(img1.shape)
# rose = img1[200:1800, 800:1900]
# img1[0:2000, 0:1000] = rose
img1.dtype = 'uint8'
# img1[:,:] = 0
# img1[100:1200, 1000:1900] = 0
img1[30:1800, 700:2900] = 100
# print(rose.shape)
# cv2.imshow("rose_ROI", rose)

cv2.imwrite("mask.png",img1)
cv2.imshow("mask",img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()