# Image Sharpness Measure for Blurred Images in Frequency Domain

## Introduction
This repository holds an implementation of the no-reference image quality assessment index proposed
by `Kanjar De and V. Masilamani` in the paper

_Image Sharpness Measure for Blurred Images in Frequency Domain_
https://www.sciencedirect.com/science/article/pii/S1877705813016007

The code was built using the Template design pattern in order to allow different dataset loading implementations.
A JSON implementation is provided, in which the input file consists of:

```json
{
    "title": "a string that represents the dataset name",
    "images": "an array of image files, initially empty",
    "image_names": "an array with the names of each image file",
    "input_folder": "the relative or absolute path of the images in the file system"
}
```

## Built With
- Python 3
- Numpy
- Imageio
- PyCodeStyle

## How to Use

```bash
# Clone the repository
$ git clone https://github.com/vaugusto92/kanjar-nr-iqa.git

# Build the docker image
$ docker build -t kanjar .

# Run the container
$ docker run -it -v $(pwd):/work kanjar bash

# Run the main script
$ ./manage.sh run <json file path>

# Run unit tests
$ ./manage.sh test

# Check pep 8 compliance of python code file
$ ./manage.sh style <python file path>

# Clear build files
$ ./manage.sh clear
```

## License 
MIT
