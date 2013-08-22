import numpy as np
from scipy.misc import imread
import matplotlib.pyplot as plt


def distance_calc(img):
    tau = 2
    xd, yd = img.shape
    for i in xd:
        for j in yd:
            img[i - tau:i + tau + 1, j - tau:j + tau + 1]


if __name__ == '__main__':
    img = imread('grass&dirt.png')

    plt.imshow(img, cmap='gray')
    plt.show()
