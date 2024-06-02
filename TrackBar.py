import numpy as np
import cv2
import matplotlib.pyplot as plt

def thresholdByTrackbar(th):
    global img

    th, bw = cv2. threshold(img, th, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('binary', bw)

img = cv2.imread('c:\computervision\mingyu.jpg', cv2.IMREAD_GRAYSCALE)

img=cv2.resize(img, dsize=(0,0), fx=0.25, fy=0.25)

cv2.imshow('binary', img)

cv2.createTrackbar('threshold', 'binary', 127, 255, thresholdByTrackbar)

cv2.waitKey()
cv2.destroyAllWindows()