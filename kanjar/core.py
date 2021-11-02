from abc import ABC, abstractmethod

import os
import sys

import imageio
import numpy as np
from termcolor import colored

class Kanjar(ABC):

    def template_method(self):

        images = [] 

        root = ''
        path = ''

        for name in images:
            print (colored('Computing image ' + str(name) + '...', 'red'))
            arr = []
            
            for j in ['1', '2', '3', '4', '5']:
                img = imageio.imread(path + name + '.BLUR.' + j + '.png')

                fft = np.fft.fftshift(np.fft.fft2(img))

                # compute the absolute value of all Fourier coefficients
                abs_val = np.abs(fft)

                # compute the maximum value among all coefficients
                M = np.max(abs_val)

                # compute the total number of coefficients that are higher than
                # the maximum value / 1000
                Th = abs_val[abs_val > M / 1000].size

                print(Th / img.size)

            np.savetxt(root + name + '-kanjar-.txt', arr, fmt='%.10f')


    def base_operation1(self):
        pass

    def base_operation2(self):
        pass

    def base_operation3(self):
        pass

    @abstractmethod
    def required_operations1(self):
        pass

    @abstractmethod
    def required_operations2(self):
        pass
