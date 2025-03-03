import numpy as np
import cv2
import time

def videoimg(videoname):
    imglist = []
    cap = cv2.VideoCapture(videoname)

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            imglist.append(frame)
        else:
            break
    return imglist

#-----------------------------------------------------------
from PIL import Image
ascii_char = list("#@&$%WMNRGPBZJIL{}?+[]()|\>;~:*"",.'' ")

def imgprocess1(r, g, b, alpha=256):
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    leng = len(ascii_char)
    percent = int(gray / 256 * leng)
    return ascii_char[percent]

def imgprocess2(img):
    im = img
    length = int(int(im.size[0])*0.18)
    width = int(int(im.size[1])*0.1)
    im = im.resize((length,width))
    txt = ""

    for y in range(width):
        for x in range(length):
            txt += imgprocess1(*im.getpixel((x, y)))
        txt += '\n'
    return txt


pro_imglist = videoimg('a.mp4')


for pic_i in range(len(pro_imglist)):
    pro_img = pro_imglist[pic_i]
    result_img = imgprocess2(pro_img)
    print(result_img)
    time.sleep(1 / 24)

