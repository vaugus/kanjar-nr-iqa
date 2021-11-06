import os
import json
import unittest

from impl import Json

class TestJsonImplementation(unittest.TestCase):

    def setUp(self):
        os.environ['TESTING'] = 'True'

    def tearDown(self):
        os.environ['TESTING'] = 'False'

    def test_load_dataset(self):
        json_impl = Json(input_file_name = './input/json/airplane.json')

        self.assertIsNotNone(json_impl)
        self.assertIsNone(json_impl.dataset)

        json_impl.load_dataset()

        self.assertIsNotNone(json_impl.dataset)

        print(json_impl.dataset)

if __name__ == '__main__':
    unittest.main()