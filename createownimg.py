#!/usr/bin/python3

import  numpy  as np
import  cv2
img=np.zeros((512,512))
img1=np.full((400,600),255)

cv2.imshow('w',img)
cv2.imshow('wi',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


