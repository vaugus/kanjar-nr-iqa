import copy
import os
import json
import unittest

from impl import JsonDataset

class TestJsonDatasetImplementation(unittest.TestCase):

    def setUp(self):
        os.environ['TESTING'] = 'True'

    def tearDown(self):
        os.environ['TESTING'] = 'False'


    def _wrap_validation_test(self, base_params, args):
        message = args.get('msg')
        validate = base_params.get('validate')

        with self.assertRaisesRegex(Exception, message):
            _dataset = copy.deepcopy(base_params.get('dataset'))
            _dataset[args.get('key')] = args.get('value')
            validate(_dataset)

    
    def test_validate_dataset(self):
        json_impl = JsonDataset(input_file_name = './input/json/airplane.json')
        dataset = json_impl.load_dataset()

        validate = json_impl.validate_dataset

        self.assertTrue(validate(dataset))

        base_params = {
            'validate': json_impl.validate_dataset,
            'dataset': dataset
        }

        assert_cases = [
            {
                'msg': 'Title is not a string.',
                'key': 'title',
                'value': 123
            },
            {
                'msg': 'Title is an empty string.',
                'key': 'title',
                'value': ''
            },
            {
                'msg': 'Title is an empty string.',
                'key': 'title',
                'value': ''
            },
            {
                'msg': 'List of images is not a list.',
                'key': 'images',
                'value': 123
            },
            {
                'msg': 'List of images has invalid initialization.',
                'key': 'images',
                'value': ['image.png']
            },
            {
                'msg': 'An image name is not a string.',
                'key': 'image_names',
                'value': [1]
            },
            {
                'msg': 'There is an empty image name.',
                'key': 'image_names',
                'value': ['']
            },
            {
                'msg': 'The input folder must be a string.',
                'key': 'input_folder',
                'value': 123
            },
            {
                'msg': 'The input folder string cannot be empty.',
                'key': 'input_folder',
                'value': ''
            },
        ]

        for case in assert_cases:
            self._wrap_validation_test(base_params, case)


    def test_load_dataset(self):
        json_impl = JsonDataset(input_file_name = './input/json/airplane.json')

        self.assertIsNotNone(json_impl)
        self.assertIsNone(json_impl.dataset)

        dataset = json_impl.load_dataset()

        self.assertIsNotNone(dataset)


if __name__ == '__main__':
    unittest.main()