import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# img = cv.imread('DSC_3430.jpg')
# img = cv.imread('/home/kyaking/downloads/pic/rose/DSC_3430.jpg')
# img = cv.imread('/home/kyaking/downloads/pic/narzissien5/IMG_6752.jpg')
img = cv.imread('/home/kyaking/downloads/pic/papri_rota/IMG_6796.JPG')

hsv = cv.cvtColor(img,cv.COLOR_RGB2HSV)
lower_hsv = np.array([35,43,46])
upper_hsv = np.array([99,255,255])
mask = cv.inRange(hsv, lowerb=lower_hsv,upperb= upper_hsv)
dst = cv.bitwise_and(img, img,mask = mask)
print("success")
# cv.imshow("plant",img)
# cv.imshow("mask",dst)
#
# cv.waitKey(0)
# cv.destroyAllWindows()
plt.imshow(dst), plt.colorbar(),plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
#
# ret,thresh1 = cv.threshold(Gray,127,255,cv.THRESH_BINARY)
# ret,thresh2=cv.threshold(Gray,127,255,cv.THRESH_BINARY_INV)
# ret,thresh3=cv.threshold(Gray,127,255,cv.THRESH_TRUNC)
# ret,thresh4=cv.threshold(Gray,127,255,cv.THRESH_TOZERO)
# ret,thresh5=cv.threshold(Gray,127,255,cv.THRESH_TOZERO_INV)
# titles = ['Gray Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [Gray, thresh1, thresh2, thresh3, thresh4, thresh5]
# for i in range(6):
#    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#    plt.title(titles[i])
#    plt.xticks([]),plt.yticks([])
# plt.show()