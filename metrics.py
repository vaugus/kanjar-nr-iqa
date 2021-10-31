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

import numpy as np
import numpy.ma as ma

from scipy.stats import kurtosis
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import normalized_root_mse, variation_of_information
from sewar.full_ref import mse, rmse, psnr, rmse_sw, uqi, ergas, scc, rase, sam, psnrb

import pywt
import imageio
import cv2

__version__ = '1.0'
__author__ = 'Victor Augusto'
__copyright__ = "Copyright (c) 2019 - Victor Augusto"


def main():
    """Main method.

    Receives a string that represents the folder with the grayscale images
    in the filesystem and computes the "Kanjar" NR-IQA index for each image.
    The images are named as "x.png", with x = [1,2...,n].

    """

    tests = {
        'cthenante': {
            'path' : '/home/victor/Documents/msc-image-database/cthenante/rgb/AxioLab/100/',
            'root' : '/home/victor/Documents/msc-data/results/IQA/data/cthenante/',
            'range': np.arange(1, 56),
            'fused': '/home/victor/Documents/msc-image-database/FUSED/cthenante/LOG.tif'},
        'callisia': {
            'path' : '/home/victor/Documents/msc-image-database/callisia/rgb/SteREO/50/',
            'root' : '/home/victor/Documents/msc-data/results/IQA/data/callisia/',
            'range': np.arange(1, 57),
            'fused': '/home/victor/Documents/msc-image-database/FUSED/callisia/LOG.tif'},
        'tradescantia': {
            'path' : '/home/victor/Documents/msc-image-database/tradescantia/rgb/SteREO/200/',
            'root' : '/home/victor/Documents/msc-data/results/IQA/data/tradescantia/',
            'range': np.arange(1, 67),
            'fused': '/home/victor/Documents/msc-image-database/FUSED/tradescantia/LOG.tif'}}

    metrics = [ssim, mse, rmse, psnr, uqi, ergas, sam, psnrb]

    for key, value in tests.items():
        fused = imageio.imread(tests[key]['fused'])[:, :2560, :]

        for metric in metrics:
            arr = []

            for i in tests[key]['range']:
                # read the image
                img = imageio.imread(tests[key]['path'] +  str(i) + '.tif')

                print(str(i) + '.tif - ' + metric.__name__)
                if metric.__name__ == 'structural_similarity':
                    res = ssim(fused, img, multichannel=True)
                else:
                    res = metric(fused, img)
                
                arr.append(res)

            # mask = imageio.imread('mask_microscopy.png')
            # gray = lambda rgb : np.dot(rgb[... , :3] , [0.299 , 0.587, 0.114]) 
            # mask = mask[:, :, None] * np.ones(3, dtype=int)[None, None, :]

            # img = np.zeros((2560, 2560, 3))
            # img[ :original_image.shape[0], :original_image.shape[1], 0] = original_image[:, :, 0]
            # img[ :original_image.shape[0], :original_image.shape[1], 1] = original_image[:, :, 1]
            # img[ :original_image.shape[0], :original_image.shape[1], 2] = original_image[:, :, 2]

            # compute the Fourier Transform with the FFT algorithm
            # fft = np.fft.fftshift(np.fft.fft2(img))
            # # fft = np.fft.fftshift(np.fft.fft2(gray(img)))
            # fft = np.multiply(fft, mask)

            # # compute the absolute value of all Fourier coefficients
            # abs_val = np.abs(fft)

            # # compute the maximum value among all coefficients
            # M = np.max(abs_val)

            # # compute the total number of coefficients that are higher than
            # # the maximum value / 1000
            # Th = abs_val[abs_val > M / 1000].size

            # metric = abs_val[abs_val > M / 1000]
            
            # # arr.append(Th / img.size)
            # arr.append(kurtosis(np.power(metric, 3)))
            # # print(Th / img.size)
            # # print(kurtosis(metric))
                
            
            # np.savetxt(root + 'FSSF-NEW.txt', arr, fmt='%.10f')
            np.savetxt(tests[key]['root'] + metric.__name__ + '.txt', arr, fmt='%.10f')

if __name__ == "__main__":
    main()
