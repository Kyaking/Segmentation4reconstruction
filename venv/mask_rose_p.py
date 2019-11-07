# encoding:utf-8
import os
import cv2 as cv
import imghdr
import time
import os


# 扫描输出图片列表
def eachFile(filepath):
    list = []
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join(filepath, allDir)
        list.append(child)
    return list

#
# # 对图片进行变形操作
# def picResize(filePath_bak):
#     files = eachFile(filePath)
#     for file in files:
#         if imghdr.what(file) in ('bmp', 'jpg', 'png', 'jpeg'):  # 判断图片的格式
#             img = cv.imread(file)  # 读取图片
#             for i in range(120, 190, 5):
#                 for j in range(120, 190, 5):
#                     res = cv.resize(img, (i, j), interpolation=cv.INTER_CUBIC)  # 借助于resize方法对图片进行处理
#                     cv.imwrite(
#                         filePath_bak + str(i) + str(j) + '_' + str(long(int(round(time.time() * 1000)))) + ".jpg",
#                         res)  # 写入目录
# 对图片进行批量的mask
def picMask(filePath_bak):
    files = eachFile(filePath)
    img2 = cv.imread('/home/kyaking/downloads/pic/rose/mask.png')
    img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
    for file in files:
        if imghdr.what(file) in ('jpg','jpeg'):
            img = cv.imread(file)
            for i in range(3428, 3463, 1):
                img_mask = cv.bitwise_and(img, img, mask=mask)
                cv.imwrite(
                    filePath_bak + 'DSC' + '_' + str(i) + ".jpg", img_mask
                )


if __name__ == '__main__':
    filePath = r"/home/kyaking/downloads/pic/rose/"
    filePath_bak = r"/home/kyaking/downloads/pic/rose_m/"
    picMask(filePath_bak)