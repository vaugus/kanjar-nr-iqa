import os
import unittest

import core

class DummyKanjarImpl(core.Kanjar):
    def load_dataset(self, **kwargs):
        return super().load_dataset(**kwargs)

class TestKanjarInterface(unittest.TestCase):

    def setUp(self):
        os.environ['TESTING'] = 'True'

    def tearDown(self):
        os.environ['TESTING'] = 'False'

    def test_empty_dataset(self):
        dummy_kanjar_impl = DummyKanjarImpl()
        self.assertIsNotNone(dummy_kanjar_impl)

        # Checks that it created a null dataset.
        self.assertIsNone(dummy_kanjar_impl.dataset)

        # Expects an Exception to be raised.
        self.assertRaises(Exception, dummy_kanjar_impl.compute_iqa())


if __name__ == '__main__':
    unittest.main()