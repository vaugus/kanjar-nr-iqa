import json

from core import Kanjar

class Json(Kanjar):

    def __init__(self, **kwargs):
        self.dataset = None
        self.input_file_name = kwargs.get('input_file_name', None)

    def load_dataset(self):
        if self.input_file_name:
            file = open(self.input_file_name)
            self.dataset = json.load(file)
            file.close()
