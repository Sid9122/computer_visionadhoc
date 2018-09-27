#!/usr/bin/python3

import  cv2
#  opencv  using  BGR color channel 
print("we are using openCV version : ",cv2.__version__)
# reading image
#          src image , image properties 
img=cv2.imread('dogs.jpg',1)  # colored 
img1=cv2.imread('dogs.jpg',0)  #  colorless grayscaled image 
print('shape of image : ',img.shape)
print(img)
imgd=img-50
imgc=img+100
halfimg=img[0:300,0:300]

#  now showing  origin size image 
cv2.imshow('adhocwindb',cv2.split(img)[0])
cv2.imshow('adhocwindg',cv2.split(img)[1])
cv2.imshow('adhocwindr',cv2.split(img)[2])
#cv2.imshow('adhoccroped',img1)
#cv2.imshow('adhoc',imgd)
#cv2.imshow('adhocq',imgc)
#writing image data into image 
cv2.imwrite('blu.jpg',img1)
cv2.imwrite('blucroped.jpg',halfimg)

# for holding  image window 
# for closing window press esc 
cv2.waitKey(0)
# to close window technically 
#cv2.destroyWindow('adhocwind')
#cv2.destroyWindow('adhoccroped')
cv2.destroyAllWindows()











