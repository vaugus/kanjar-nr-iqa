# Image Sharpness Measure for Blurred Images in Frequency Domain

## Introduction
This repository holds an implementation of the no-reference image quality assessment index proposed
by `Kanjar De and V. Masilamani` in the paper

_Image Sharpness Measure for Blurred Images in Frequency Domain_
https://www.sciencedirect.com/science/article/pii/S1877705813016007

## Built With
- Python 3
- Numpy
- imageio
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
