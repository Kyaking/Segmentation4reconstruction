import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('/home/kyaking/downloads/pic/rose/DSC_3430.jpg',0)# queryImage
img2 = cv2.imread('/home/kyaking/downloads/pic/rose/DSC_3431.jpg',0) # trainImage

# Initiate SIFT detector
orb = cv2.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
print(len(kp1))

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=False)
# bf = cv.BFMatcher_create(cv2.NORM_L2, crossCheck=False)
# Match descriptors.
matches = bf.match(des1, des2)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

# Draw first 10 matches.
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:], None,flags=2)
plt.imshow(img3),plt.show()
cv2.imshow('drawMatches',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
