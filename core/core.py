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

This class implements the no-reference image quality assessment index proposed
by Kanjar De and V. Masilamani in the paper

"Image Sharpness Measure for Blurred Images in Frequency Domain"
https://www.sciencedirect.com/science/article/pii/S1877705813016007

"""


import logging
import os
from abc import ABC, abstractmethod

import imageio
import numpy as np

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

__version__ = '2.0'
__author__ = 'Victor Augusto'
__copyright__ = "Copyright (c) 2019 - Victor Augusto Alves Catanante"


class Kanjar(ABC):

    def compute_iqa(self, dataset):

        try:
            if not dataset:
                raise Exception('The dataset was not initialized.')

            results = []
            for name in dataset.get('image_names'):
                logging.info('Computing image ' + str(name))

                image = imageio.imread(dataset.get('input_folder') + name)

                fourier_coefficients = np.fft.fftshift(np.fft.fft2(image))

                # compute the absolute value of all Fourier coefficients
                abs_values = np.abs(fourier_coefficients)

                # compute the maximum value among all coefficients
                maximum_value = np.max(abs_values)

                # compute the total number of coefficients that are higher than
                # the maximum value / 1000
                total = abs_values[abs_values > maximum_value / 1000].size

                results.append(total / image.size)

            output = 'output/' + dataset.get('title') + '-kanjar.txt'
            np.savetxt(output, results, fmt='%.10f')

        except Exception as e:
            if 'False' == os.getenv('TESTING'):
                logging.error(e.args)

    @abstractmethod
    def load_dataset(self, **kwargs):
        pass
