import cv2
import numpy as np


if __name__ == '__main__':

    fname = 'data/images/score_3.png'
    img = cv2.imread(fname)
    img_size = img.shape[:2]

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh, img_bw = cv2.threshold(img_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    edges = cv2.Canny(img_bw, 50, 150, apertureSize=3)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 150, None, 0, 0)
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv2.imwrite('data/images/score_2_lines.jpg', img)
