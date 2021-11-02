from abc import ABC, abstractmethod

import imageio
import numpy as np

from typing import NamedTuple
from termcolor import colored

class DataSet:

    def __init__(self):
        self.title = ''
        self.images = []
        self.image_names = []
        self.input_folder = ''
        self.output_folder = ''

class Kanjar(ABC):

    def __init__(self):
        self.dataset = DataSet()

    def compute_iqa(self):

        dataset = self.dataset

        for name in dataset.image_names:
            print (colored('Computing image ' + str(name) + '...', 'red'))
            arr = []
            
            img = imageio.imread(dataset.input_folder + name)

            fft = np.fft.fftshift(np.fft.fft2(img))

            # compute the absolute value of all Fourier coefficients
            abs_val = np.abs(fft)

            # compute the maximum value among all coefficients
            M = np.max(abs_val)

            # compute the total number of coefficients that are higher than
            # the maximum value / 1000
            Th = abs_val[abs_val > M / 1000].size

            print(Th / img.size)

        output = dataset.output_folder + dataset.title + '-kanjar-.txt'
        np.savetxt(output, arr, fmt='%.10f')


    @abstractmethod
    def load_images(self):
        pass

    @abstractmethod
    def load_image_names(self):
        pass

    @abstractmethod
    def load_input_folder(self):
        pass

    @abstractmethod
    def load_output_folder(self):
        pass

