from PIL import ImageGrab, ImageColor
import numpy as np

box1 = (10, 10, 20, 20)
#box2 = (xi2, yi2, xf2, yf2)

while True:
    left_box = ImageGrab.grab(box1)
    #right_box = ImageGrab.grab(box2)

    left_color = ImageColor.getrgb(left_box)
    print(left_color)

    # print('##########')
    # right_color = ImageColor.getrgb(right_box)
    # print(right_color)