#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from impl import JsonDataset


def main():
    json_impl = JsonDataset(input_file_name='./input/json/airplane.json')
    dataset = json_impl.load_dataset()

    dataset['output_folder'] = ''

    json_impl.compute_iqa(dataset)


if __name__ == '__main__':
    main()
