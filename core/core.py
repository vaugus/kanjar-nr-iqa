from abc import ABC, abstractmethod
import os

import imageio
import numpy as np

from typing import NamedTuple
from termcolor import colored

# JSON: file format, image base name

class Kanjar(ABC):

    def __init__(self):
        self.dataset = None

    def compute_iqa(self):

        self.load_dataset()

        try:
            if not self.dataset:
                raise Exception('The dataset was not initialized.')
        
            dataset = self.dataset

            for name in dataset.image_names:
                message = 'Computing image ' + str(name) + '...'
                print(colored(message, 'red'))
                results = []
                
                image = imageio.imread(dataset.input_folder + name)

                fourier_coefficients = np.fft.fftshift(np.fft.fft2(image))

                # compute the absolute value of all Fourier coefficients
                abs_values = np.abs(fourier_coefficients)

                # compute the maximum value among all coefficients
                maximum_value = np.max(abs_values)

                # compute the total number of coefficients that are higher than
                # the maximum value / 1000
                total = abs_values[abs_values > maximum_value / 1000].size

                results.append(total / image.size)

            output = dataset.output_folder + dataset.title + '-kanjar-.txt'
            np.savetxt(output, results, fmt='%.10f')

        except Exception as e:
            if 'False' == os.getenv('TESTING'):
                print(e)


    @abstractmethod
    def load_dataset(self, **kwargs):
        pass


