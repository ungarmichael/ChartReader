# calculating the values using the 
# * reader
# * xaxis
# * yaxis
# * chart
# classes

from reader import Reader
from chart import Chart
import numpy as np
import cv2 as cv

def presi():
    img = cv.imread('./input/1.png')
    cv.imshow('1.jpg',img)
    print(img[343,160])
    cv.waitKey(0)

def main():
    values = Reader.loadImageIntoPixels('./input/1.png')
    res = Chart.readTheDarkestValue(values[10])
    print(res)

if __name__ == "__main__":
    main()