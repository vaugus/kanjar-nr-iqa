from abc import ABC, abstractmethod

import imageio
import numpy as np
import termcolor.colored as colored

class Kanjar(ABC):

    def compute_iqa(self, input_folder, output_folder, images):

        for name in images:
            print (colored('Computing image ' + str(name) + '...', 'red'))
            arr = []
            
            img = imageio.imread(input_folder + name)

            fft = np.fft.fftshift(np.fft.fft2(img))

            # compute the absolute value of all Fourier coefficients
            abs_val = np.abs(fft)

            # compute the maximum value among all coefficients
            M = np.max(abs_val)

            # compute the total number of coefficients that are higher than
            # the maximum value / 1000
            Th = abs_val[abs_val > M / 1000].size

            print(Th / img.size)

        np.savetxt(output_folder + '-kanjar-.txt', arr, fmt='%.10f')


    @abstractmethod
    def required_operations1(self):
        pass

    @abstractmethod
    def required_operations2(self):
        pass
