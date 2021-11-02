from abc import ABC, abstractmethod

import imageio
import numpy as np

from typing import NamedTuple
from termcolor import colored


class Kanjar(ABC):

    def compute_iqa(self):

        # TODO: somehow instantiate the dataset 
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

