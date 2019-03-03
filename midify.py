import cv2
import numpy as np
from test import staffLines

WHITE = 200
BLACK = 100


if __name__ == '__main__':

    fname = 'data/images/score_3.png'
    img = cv2.imread(fname)
    img_c = img.copy()
    img_size = img.shape[:2]

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = 150
    img_bw = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY)[1]

    edges = cv2.Canny(img_bw, 50, 150, apertureSize=3)
    p_lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 150, 100, 0, 0)
    # for line in p_lines:
    #     for x1, y1, x2, y2 in line:
    #         cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

    #print(len(p_lines))
    p_lines, min_x, max_x = staffLines(p_lines)

    for line in p_lines:
        cv2.line(img, (min_x, line), (max_x, line), (0, 0, 255), 2)

    cv2.imwrite('data/images/score_3_lines.jpg', img)



    # y = 0
    # while y < img_size[0] - 10:
    #     print(y)
    #     x = 0
    #     white = True
    #     while x < img_size[1] - 10:
    #         colors = 0
    #         for y2 in range(y, y + 10):
    #             for x2 in range(x, x + 10):
    #                 pixel_color = img[y2, x2]
    #                 if pixel_color[0] < 200:
    #                     colors += 0
    #                 else:
    #                     colors += 255
    #         colors /= 100
    #         if colors >= WHITE:
    #             x += 10
    #         elif colors <= BLACK:
    #             img_c[y, x] = [0, 0, 255]
    #             white = False
    #             x += 1
    #         else:
    #             white = False
    #             x += 1
    #     if white:
    #         y += 10
    #     else:
    #         y += 1
    #
    # cv2.imwrite('data/images/score_3_lines.jpg', img_c)



    # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # thresh = 150
    # img_bw = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY)[1]
    #
    # # edges = cv2.Canny(img_bw, 50, 150, apertureSize=3)
    # # p_lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 150, 100, 0, 0)
    # # for line in p_lines:
    # #     for x1, y1, x2, y2 in line:
    # #         cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    #
    # circles = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, 1, 5, param1=250, param2=20, minRadius=1, maxRadius=10)
    # print(circles)
    # circles = np.uint16(np.around(circles))
    # print(circles)
    # for i in circles[0, :]:
    #     # draw the outer circle
    #     cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    #     # draw the center of the circle
    #     cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
    #
    # cv2.imwrite('data/images/score_3_lines.jpg', img)
