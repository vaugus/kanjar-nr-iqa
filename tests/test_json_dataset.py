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

    
    def test_validate_dataset(self):
        json_impl = JsonDataset(input_file_name = './input/json/airplane.json')
        dataset = json_impl.load_dataset()

        validate = json_impl.validate_dataset

        validate(dataset)

        with self.assertRaisesRegex(Exception, 'Title is not a string.') as e:
            _dataset = copy.deepcopy(dataset)
            _dataset['title'] = 123
            validate(_dataset)

        with self.assertRaisesRegex(Exception, 'Title is an empty string.') as e:
            _dataset = copy.deepcopy(dataset)
            _dataset['title'] = ''
            validate(_dataset)


    def test_load_dataset(self):
        json_impl = JsonDataset(input_file_name = './input/json/airplane.json')

        self.assertIsNotNone(json_impl)
        self.assertIsNone(json_impl.dataset)

        dataset = json_impl.load_dataset()

        self.assertIsNotNone(dataset)


if __name__ == '__main__':
    unittest.main()