import cv2
import numpy as np

img = cv2.imread("C:\computervision\dog.jpg")
#img = cv2.resize(img, dsize=(0, 0), fx= 0.25, fy= 0.25)
img_disp = np.copy(img)

mask = np.zeros((img.shape[0], img.shape[1]), np.uint8)
mask[:, :] = cv2.GC_PR_BGD

brushSize = 5
color_B, color_R = (255,0,0),(0,0,255)

def painting(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img_disp, (x, y), brushSize, color_B, -1)
        cv2.circle(mask, (x, y), brushSize, cv2.GC_FGD, -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img_disp, (x, y), brushSize, color_R, -1)
        cv2.circle(mask, (x, y), brushSize, cv2.GC_BGD, -1)
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img_disp, (x, y), brushSize, color_B, -1)
        cv2.circle(mask, (x, y), brushSize, cv2.GC_FGD, -1)
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_RBUTTON:
        cv2.circle(img_disp, (x, y), brushSize, color_R, -1)
        cv2.circle(mask, (x, y), brushSize, cv2.GC_BGD, -1)
    cv2.imshow("painting", img_disp)

def seg_grabcut():
    bgd = np.zeros((1, 65), np.float64)
    fgd = np.zeros((1, 65), np.float64)

    cv2.grabCut(img, mask, None, bgd, fgd, 5, cv2.GC_INIT_WITH_MASK)
    mask2 = np.where((mask==cv2.GC_BGD)|(mask==cv2.GC_PR_BGD), 0, 1).astype('uint8')
    grab = img*mask2[:, :, np.newaxis]
    cv2.imshow('result', grab)

cv2.namedWindow("painting")
cv2.imshow('painting', img_disp)
cv2.setMouseCallback('painting', painting)

while(True):
    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()
        break
    elif key == ord('s'):
        seg_grabcut()
