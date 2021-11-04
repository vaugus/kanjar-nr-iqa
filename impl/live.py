import json

from core import Kanjar

class Live(Kanjar):

    def load_dataset(self, **kwargs):
        input_file_name = kwargs.get('input_file_name', None)

        if input_file_name:
            file = open(input_file_name)
            return json.load(file)

        return None
