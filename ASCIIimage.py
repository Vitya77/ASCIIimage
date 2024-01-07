import cv2 as cv
from math import floor
import os

density = 'Ñ@#W$9876543210?!abc;:+=-,._    '
density_inv = density[::-1]

video = cv.VideoCapture(0)
while True:
    ret, frame = video.read()

    resized_frame = cv.resize(frame, (100, 40))

    height, width, channels = resized_frame.shape

    rows = ''
    for i in range(height):
        row = ''
        for j in range(width):
            b, g, r = resized_frame[i, j]
            index_of_symbol = floor((((b + g + r)/3)/255)*len(density))
            row += density[index_of_symbol]
        rows += row + '\n'

    cv.imshow('Frame', frame)
    print(rows)
    os.system('cls')
    

    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video.release()