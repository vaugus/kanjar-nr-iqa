import json
import logging
import traceback

import imageio

from core import Kanjar

spec_errors = {
    'assert isinstance(dataset.get(\'title\'), str)': 
        'Title is not a string.',
    'assert bool(dataset.get(\'title\').strip())':
        'Title is an empty string.',
    'assert isinstance(dataset.get(\'images\'), list)':
        'List of images is not a list.',
    'assert not dataset.get(\'images\')':
        'List of images has invalid initialization.',
    'assert isinstance(img, str)':
        'An image name is not a string.',
    'assert bool(img.strip())':
        'There is an empty image name.',
    'assert isinstance(dataset.get(\'input_folder\'), str)':
        'The input folder must be a string.',
    'assert bool(dataset.get(\'input_folder\').strip())':
        'The input folder string cannot be empty.'
    }


class JsonDataset(Kanjar):


    def __init__(self, **kwargs):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        self.dataset = None
        self.input_file_name = kwargs.get('input_file_name', None)


    def compose(self, current_value, *args):
        for function in args:
            current_value = function(current_value)
        return current_value


    def _parse_assert_error(self, error):
        traceback_msg = self.compose(error.__traceback__,
                                     traceback.format_tb,
                                     ''.join)

        split_traceback = traceback_msg.split('\n')
        return split_traceback[1].strip()


    def _assert_message(self, assert_error):
        return spec_errors[assert_error]


    def validate_dataset(self, dataset):
        valid = True
        message = None

        try:
            assert isinstance(dataset.get('title'), str)
            assert bool(dataset.get('title').strip())

            assert isinstance(dataset.get('images'), list)
            assert not dataset.get('images')

            assert isinstance(dataset.get('image_names'), list)
            assert dataset.get('image_names')

            for img in dataset.get('image_names'):
                assert isinstance(img, str)
                assert bool(img.strip())

            assert isinstance(dataset.get('input_folder'), str)
            assert bool(dataset.get('input_folder').strip())

        except AssertionError as e:
            assert_error = self._parse_assert_error(e)
            message = self._assert_message(assert_error)
            valid = False

        if not valid:
            raise Exception(message)
            
        return valid


    def load_images(self, folder, file_names):
        images = []

        for name in file_names:
            img = imageio.imread(folder + name)
            images.append(img)

        return images


    def load_dataset(self):
        dataset = None
        images = None

        try:
            if self.input_file_name:
                file = open(self.input_file_name)
                dataset = json.load(file)
                file.close()

            is_dataset_valid = self.validate_dataset(dataset)

            if is_dataset_valid:
                images = self.load_images(dataset.get('input_folder'), 
                                          dataset.get('image_names'))

            dataset['images'] = images
            return dataset

        except Exception as e:
            logging.error(e.args)
