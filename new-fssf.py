#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# MIT License
#
# Copyright (c) 2020 Victor Augusto
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Computes a Fourier Transform based NR-IQA index.

This script implements the no-reference image quality assessment index proposed
by Kanjar De and V. Masilamani in the paper

"Image Sharpness Measure for Blurred Images in Frequency Domain"
https://www.sciencedirect.com/science/article/pii/S1877705813016007

"""

import os
import sys

import numpy as np

from scipy.stats import kurtosis

import pywt
import imageio
import cv2
from termcolor import colored
from skimage.metrics import normalized_root_mse as nrmse


__version__ = '1.0'
__author__ = 'Victor Augusto'
__copyright__ = "Copyright (c) 2019 - Victor Augusto"


def main():
    """Main method.

    Receives a string that represents the folder with the grayscale images
    in the filesystem and computes the "Kanjar" NR-IQA index for each image.
    The images are named as "x.png", with x = [1,2...,n].

    """
    path = sys.argv[1]
    mask_path = sys.argv[2]
    param = int(sys.argv[3])

    path="/home/victor/Documents/msc-image-database/KADID/kadid10k/images/"
    mask_path="mask_kadid.png"

    images = [int(x) for x in sys.argv[4:]]

    root="/home/victor/Documents/msc-data/results/IQA/data/kadid/"

    mask = imageio.imread(mask_path)
    mask = mask[:, :, None] * np.ones(3, dtype=int)[None, None, :]


    for i in images:
        print (colored('Computing image ' + str(i) + '...', 'red'))
        arr = []
        image_name = 'I'
        if i < 10:
            image_name += '0' + str(i)
        else:
            image_name += str(i)

        truth = imageio.imread(path + image_name + '.png')
        
        for j in ['01', '02', '03', '04', '05']:
            name = path + image_name + '_01_' + j + '.png'
            img = imageio.imread(name)

            arr.append(nrmse(truth, img))

        np.savetxt(root + image_name + '-NRMSE.txt', arr, fmt='%.10f')

    # mask = imageio.imread(mask_path)
    # mask = mask[:, :, None] * np.ones(3, dtype=int)[None, None, :]


    # for i in images:
    #     print (colored('Computing image ' + str(i) + '...', 'red'))
    #     arr = []
    #     image_name = 'I'
    #     if i < 10:
    #         image_name += '0' + str(i)
    #     else:
    #         image_name += str(i)
        
    #     for j in ['01', '02', '03', '04', '05']:
    #         name = path + image_name + '_01_' + j + '.png'
    #         img = imageio.imread(name)

    #         # compute the Fourier Transform with the FFT algorithm
    #         fft = np.fft.fftshift(np.fft.fft2(img))
    #         fft = np.multiply(fft, mask)

    #         # compute the absolute value of all Fourier coefficients
    #         abs_val = np.abs(fft)

    #         # compute the maximum value among all coefficients
    #         M = np.max(abs_val)

    #         # compute the total number of coefficients that are higher than
    #         # the maximum value / 1000
    #         metric = abs_val[abs_val > M / param]
        
    #         # arr.append(kurtosis(np.power(metric, 3)))
    #         arr.append(kurtosis(metric))

    #     np.savetxt(root + image_name + '-FSSF-NEW.txt', arr, fmt='%.10f')

if __name__ == "__main__":
    main()
