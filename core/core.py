from abc import ABC, abstractmethod
import logging
import os

import imageio
import numpy as np

from typing import NamedTuple
from termcolor import colored

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

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


