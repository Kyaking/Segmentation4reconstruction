import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# img = cv.imread('DSC_3430.jpg')
img = cv.imread('/home/kyaking/downloads/pic/rose/DSC_3430.jpg')
# img = cv.imread('/home/kyaking/downloads/pic/narzissien5/IMG_6752.jpg')
# cv.cvtColor(img , img , CV_RGBA2RGB)
img = cv.resize(img,)
# img = cv.cvtColor(img, cv.COLOR_RGB2YCrCb)
# gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (1200,150,550,1100)
cv.grabCut(img,mask,rect,bgdModel,fgdModel,200,cv.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
# plt.imshow(mask2),plt.colorbar(),plt.show()
plt.imshow(img), plt.colorbar(),plt.show()
# newmask = cv.imread('/home/kyaking/downloads/pic/rose/DSC_3430.jpg',0)

