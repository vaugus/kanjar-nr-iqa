#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import os
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

    # Redefs for the load images function
    def mock_load_images(self, folder, file_names):
        return []

    def test_validate_dataset(self):
        json_impl = JsonDataset(input_file_name='./input/json/airplane.json')

        json_impl.load_images = self.mock_load_images
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
        json_impl = JsonDataset(input_file_name='./input/json/airplane.json')

        # Original function
        load_images = json_impl.load_images
        self.assertIsNotNone(json_impl)
        self.assertIsNone(json_impl.dataset)

        json_impl.load_images = self.mock_load_images
        dataset = json_impl.load_dataset()
        self.assertIsNotNone(dataset)

        json_impl.load_images = load_images
        dataset = json_impl.load_dataset()
        self.assertIsNotNone(dataset)

    def test_compute_iqa(self):
        json_impl = JsonDataset(input_file_name='./input/json/airplane.json')
        dataset = json_impl.load_dataset()

        dataset['output_folder'] = ''

        json_impl.compute_iqa(dataset)


if __name__ == '__main__':
    unittest.main()
