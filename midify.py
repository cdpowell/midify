import cv2
import numpy as np

WHITE = 200
BLACK = 100


if __name__ == '__main__':

    fname = 'data/images/score_3.png'
    img = cv2.imread(fname)
    img_c = img.copy()
    img_size = img.shape[:2]
    print(img_size)

    y = 0
    while y < img_size[0] - 10:
        print(y)
        x = 0
        white = True
        while x < img_size[1] - 10:
            colors = 0
            for y2 in range(y, y + 10):
                for x2 in range(x, x + 10):
                    pixel_color = img[y2, x2]
                    if pixel_color[0] < 200:
                        colors += 0
                    else:
                        colors += 255
            colors /= 100
            if colors >= WHITE:
                x += 10
            elif colors <= BLACK:
                img_c[y, x] = [0, 0, 255]
                white = False
                x += 1
            else:
                white = False
                x += 1
        if white:
            y += 10
        else:
            y += 1

    cv2.imwrite('data/images/score_3_lines.jpg', img_c)

    # x = 0
    # while x < img_size[1] - 10:
    #     y = 0
    #     print(x)
    #     white = True
    #     while y < img_size[0] - 10:
    #         colors = [0, 0, 0]
    #         for x2 in range(x, x + 10):
    #             for y2 in range(y, y + 10):
    #                 pixel_color = img[y2, x2]
    #                 colors[0] += pixel_color[0]
    #                 colors[1] += pixel_color[1]
    #                 colors[2] += pixel_color[2]
    #         for c in range(len(colors)):
    #             colors[c] /= 100
    #         if colors[0] >= 200 and colors[1] >= 200 and colors[2] >= 200:
    #             y += 10
    #         else:
    #             white = False
    #             y += 1
    #     if white:
    #         x += 10
    #     else:
    #         x += 1

    # for x in range(img_size[1] - 10):
        # for y in range(img_size[0] - 10):
        #     print(y, x)
        #     colors = [0, 0, 0]
        #     for x2 in range(x, x + 11):
        #         for y2 in range(y, y + 10):
        #             pixel_color = img[y2, x2]
        #             colors[0] += pixel_color[0]
        #             colors[1] += pixel_color[1]
        #             colors[2] += pixel_color[2]
        #     for c in range(len(colors)):
        #         colors[c] /= 110


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
