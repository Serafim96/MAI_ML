import numpy as np
import cv2 as cv

def nothing(x):
    pass

img = cv.imread('sudoku.png')
cv.namedWindow('image')
cv.createTrackbar('thresh1','image',100,255,nothing)
cv.createTrackbar('thresh2','image',255,255,nothing)
cv.createTrackbar('aperture','image',3,7,nothing)
cv.createTrackbar('L2gradient','image',0,1,nothing)
while(1):
    t1 = cv.getTrackbarPos('thresh1','image')
    t2 = cv.getTrackbarPos('thresh2','image')
    a = max(cv.getTrackbarPos('aperture','image'), 3)
    if a % 2 == 0:
        a += 1
    cv.setTrackbarPos('aperture','image',a)
    s = cv.getTrackbarPos('L2gradient','image')
    edges = cv.Canny(img, threshold1=t1, threshold2=t2, apertureSize=a, L2gradient=(s==1))
    #print(edges)
    cv.imshow('image',edges)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()