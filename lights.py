from PIL import ImageGrab, ImageColor
import numpy as np
import serial
import time

box1 = (1200, 400, 1202, 402)
box2 = (2020, 400, 2022, 402)

left_touch = False
right_touch = False
current_msg = str('waiting')
previous_msg = str('a')
x = 0

communication = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(1)

while True:
    left_box = ImageGrab.grab(box1)
    right_box = ImageGrab.grab(box2)

    left_color = np.array(left_box.getcolors())
    left_tuple = left_color[0,1]
    left_red = left_tuple[0]
    left_green = left_tuple[1]
    left_blue = left_tuple[2]

    if left_red > 240 and left_green < 200 and left_blue < 200:
        left_touch = True
        if right_touch == False:
            current_msg = 'left'
            x = 1
        elif right_touch == True:
            current_msg = 'both'
            x = 3
    
    right_color = np.array(right_box.getcolors())
    right_tuple = right_color[0,1]
    right_red = right_tuple[0]
    right_green = right_tuple[1]
    right_blue = right_tuple[2]

    if right_green > 240 and right_red < 200 and right_blue < 200:
        right_touch = True
        if left_touch == False:
            current_msg = 'right'
            x = 2
        elif left_touch == True:
            current_msg = 'both'
            x = 3

    if current_msg is not previous_msg:
        print (current_msg)
        if x == 1:
            communication.write(b'1')
        elif x == 2:
            communication.write(b'2')
        elif x == 3:
            communication.write(b'3')
        previous_msg = current_msg    

    else:
        right_touch = False
        left_touch = False
        current_msg = 'waiting'
        x = 0
        communication.write(b'0')