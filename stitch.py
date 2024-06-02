import cv2
#import numpy as np
import sys

#cap = cv2.VideoCapture(0)
#if not cap.isOpend(): sys.exit("camera open failed")

img_1 = cv2.imread("C:\computervision\mm_view_1.jpg")
img_2 = cv2.imread("C:\computervision\mm_view_2.jpg")
img_3 = cv2.imread("C:\computervision\mm_view_3.jpg")
img_4 = cv2.imread("C:\computervision\mm_view_4.jpg")

imgs = [img_1,img_2,img_3,img_4]

stitcher = cv2.Stitcher_create()
status, dst = stitcher.stitch(imgs)
if status == cv2.STITCHER_OK:
    cv2.imshow("image stitched panorama", dst)
else:
    print("error on stitching!")
    sys.exit()
cv2.imshow("img_1", img_1)
cv2.imshow("img_2", img_2)
cv2.imshow("img_3", img_3)
cv2.imshow("img_4", img_4)
cv2.imshow("result_panorama", dst)
cv2.imwrite("result_panorama.jpg", dst)

cv2.waitKey()
cv2.destroyAllWindows()