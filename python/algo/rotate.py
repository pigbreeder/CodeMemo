#encoding=utf8
import cv2
import numpy as np
# 旋转矩阵
# https://www.cnblogs.com/zhoug2020/p/7842808.html
# https://blog.csdn.net/qq_30019237/article/details/81007214
def rotate(img='rotate.jpg', angle=30):
    theta = np.deg2rad(angle)
    img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    row,col = img.shape
    row_r = np.round(np.abs(row * np.cos(theta)) + np.abs(col*np.sin(theta)))
    col_r = np.round(np.abs(col * np.cos(theta)) + np.abs(row*np.sin(theta)))
    row_r,col_r = int(row_r), int(col_r)
    new_img = np.zeros((row_r, col_r))
    for i in range(row_r):
        for j in range(col_r):
            ii = i - row_r / 2
            jj = j - col_r / 2
            x = ii * np.cos(theta) - jj * np.sin(theta)
            y = jj * np.cos(theta) + ii * np.sin(theta)
            x = int(np.round(x + row_r / 2))
            y = int(np.round(y + col_r / 2))
            if x > 0 and x < row and y > 0 and y < col:
                # print(i,j,x,y)
                new_img[i,j] = img[x,y]
    return new_img

r = rotate()
cv2.imwrite('q.jpg', r)