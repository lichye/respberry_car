import cv2
import numpy as np
import time

img=cv2.imread('caochang.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('img',img)

retval,dst=cv2.threshold(img,0,255,cv2.THRESH_OTSU)
cv2.imshow('dst',dst)
kernel = np.ones((2,2),np.uint8)
kernel2 = np.ones((5,5),np.uint8)
dst2=cv2.erode(dst,kernel,iterations=2)
dst1 = cv2.dilate(dst2,kernel,iterations=5)

dst2=cv2.erode(dst1,kernel,iterations=2)
cv2.imshow('dst1',dst2)

dst1 = cv2.dilate(dst2,kernel,iterations=5)
dst2=cv2.erode(dst1,kernel2,iterations=4)
cv2.imshow('dst2',dst1)
kernel3=np.ones((6,6),np.uint8)
dst1 = cv2.dilate(dst2,kernel2,iterations=5)
cv2.imshow('ds3',dst2)
cv2.imshow('dst4',dst1)
dst1 = cv2.dilate(dst2,kernel2,iterations=30)
cv2.imshow('dst5',dst1)
