from PIL import ImageGrab, ImageColor
from numpy import *

box1 = (1200, 400, 1202, 402)
box2 = (2020, 400, 2022, 402)
left_touch = False
right_touch = False

while True:
    left_box = ImageGrab.grab(box1)
    right_box = ImageGrab.grab(box2)

    left_color = array(left_box.getcolors())
    left_tuple = left_color[0,1]
    left_red = left_tuple[0]
    left_green = left_tuple[1]
    left_blue = left_tuple[2]
    
    print(left_touch)

    if left_red > 240 and left_green < 200 and left_blue < 200 and right_touch == False:
        left_touch = True
        print('LEFT TOUCHED!!!')
    
    right_color = array(right_box.getcolors())
    right_tuple = right_color[0,1]
    right_red = right_tuple[0]
    right_green = right_tuple[1]
    right_blue = right_tuple[2]

    if right_green > 240 and right_red < 200 and right_blue < 200 and left_touch == False:
        right_touch = True
        print('RIGHT TOUCHED!!!')

    elif right_touch == True and left_touch == True:
        print('BOTH TOUCHED!!!')
    
    else:
        right_touch = False
        left_touch = False
