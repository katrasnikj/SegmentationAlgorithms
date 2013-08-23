import numpy as np
from scipy.misc import imread
import matplotlib.pyplot as plt


def distance_calc(img):
    tau = 5
    sigma = 1.5
    xd, yd = img.shape
    img = img.astype('float64')
    img = img/np.max(img)
    result = np.zeros_like(img)
    for i in range(xd):
        for j in range(yd):
            if i - tau >= 0 and i + tau < xd and j - tau >= 0 and j + tau < yd:
                #import pdb;pdb.set_trace()
                tmp = img[i - tau:i + tau + 1, j - tau:j + tau + 1]
                gx, gy = np.gradient(tmp)
                Mg = np.vstack((np.hstack((1 + gx**2, gx*gy)),
                                np.hstack((gx*gy, 1 + gy**2))))
                F = np.exp(-np.linalg.det(Mg)/sigma**2)
                result[i, j] = F
    return result

if __name__ == '__main__':
    img = imread('grass&dirt.png')
    result = distance_calc(img)
    plt.subplot(121)
    plt.imshow(img, cmap='gray')
    plt.subplot(122)
    plt.imshow(result[10:-10, 10:-10])
    plt.colorbar()
    plt.show()


    #plt.imshow(img, cmap='gray')
    #plt.show()
