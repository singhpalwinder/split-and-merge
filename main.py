from cv2 import namedWindow, imshow, waitKey, imwrite, imread

from numpy import zeros, ones, array, shape, arange, concatenate




import numpy as np

def split_and_combine(image1, image2):
    height, width, channels = image1.shape
    middle = width // 2
    left1 = image1[:, :middle, :]
    right2 = image2[:, middle:, :]

    result = zeros((height, width, channels), dtype=np.uint8)
    result[:height, :middle, :] = left1
    result[:height, middle:, :] = right2
    return result


image1 = imread("original.png")
image2 = imread("edited.png")
result = split_and_combine(image1, image2)
imwrite("result.jpg", result)

 

