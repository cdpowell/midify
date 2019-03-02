import cv2
import numpy as np


if __name__ == '__main__':

    fname = 'data/images/score_3.png'
    img = cv2.imread(fname)
    img_size = img.shape[:2]

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = 150
    img_bw = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY)[1]

    edges = cv2.Canny(img_bw, 50, 150, apertureSize=3)
    p_lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 150, 100, 0, 0)
    # circles = cv2.HoughCircles(img_bw, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=100, minRadius=0, maxRadius=0)
    # circles = np.uint16(np.around(circles))

    for line in p_lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    # circles = np.uint16(np.around(circles))
    # print(circles)
    # for i in circles[0, :]:
    #     # draw the outer circle
    #     cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    #     # draw the center of the circle
    #     cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

    # lines = cv2.HoughLines(edges, 1, np.pi / 180, 150, None, 0, 0)
    # for line in p_lines:
    #     for x1, y1, x2, y2 in line:
    #         cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imwrite('data/images/score_3_bw.jpg', img_bw)
    cv2.imwrite('data/images/score_3_lines.jpg', img)
