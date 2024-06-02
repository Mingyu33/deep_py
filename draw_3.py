import cv2
import sys

img = cv2.imread("C:\computervision\mingyu.jpg")

if img is None:
    sys.exit("cannot find the file.")

img = cv2.resize(img, dsize=(0, 0), fx= 0.25, fy= 0.25)

def draw(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(img, (x, y), (x+200, y+200), (0, 0, 255), 2)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(img, (x, y), (x+100, y+100), (255, 0, 0), 2)
    cv2.imshow("draw", img)

def draw_drag(event, x, y, flags, param):
    global gx, gy

    if event == cv2.EVENT_LBUTTONDOWN:
        gx, gy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.rectangle(img, (gx, gy), (x, y), (0, 0, 255), 2)
    cv2.imshow("draw", img)

brush_size = 5
color_B, color_R = (255, 0, 0), (0, 0, 255)

def draw_curve(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), brush_size, color_B, -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), brush_size, color_R, -1)
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img, (x, y), brush_size, color_B, -1)
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_RBUTTON:
        cv2.circle(img, (x, y), brush_size, color_R, -1)
    cv2.imshow("draw", img)

cv2.namedWindow("draw")
cv2.imshow("draw", img)

#cv2.setMouseCallback("draw", draw)
#cv2.setMouseCallback("draw", draw_drag)
cv2.setMouseCallback("draw", draw_curve)

while(True):
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break