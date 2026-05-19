# Image Sharpness Measure for Blurred Images in Frequency Domain

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3-blue.svg)](https://www.python.org/)

## 🌟 Overview

This repository contains an implementation of the no-reference image quality assessment (NR-IQA) index proposed by `Kanjar De and V. Masilamani` in the paper:

> *Image Sharpness Measure for Blurred Images in Frequency Domain*
> [https://www.sciencedirect.com/science/article/pii/S1877705813016007](https://www.sciencedirect.com/science/article/pii/S1877705813016007)

The project evaluates image sharpness in the frequency domain without requiring a reference image. The implementation follows the Template Design Pattern to support multiple dataset loading strategies.

A JSON-based dataset loader is included by default.

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/vaugusto92/kanjar-nr-iqa.git

# Enter the project directory
cd kanjar-nr-iqa

# Build the Docker image
docker build -t kanjar .

# Run the container
docker run -it -v $(pwd):/work kanjar bash

# Execute the sharpness evaluation
./manage.sh run <json file path>
```

---

## 🛠️ Prerequisites

Before running the project, ensure the following tools are installed:

* Docker
* Python 3

### Python Dependencies

The project uses the following libraries:

* Numpy
* Imageio
* PyCodeStyle

If you prefer running locally instead of Docker, install the dependencies manually:

```bash
pip install -r requirements.txt
```

---

## 📚 Dataset Format

The included JSON loader expects input files in the following format:

```json
{
    "title": "Dataset name",
    "images": [],
    "image_names": [
        "image1.png",
        "image2.png"
    ],
    "input_folder": "/path/to/images"
}
```

### Field Description

| Field          | Description                                      |
| -------------- | ------------------------------------------------ |
| `title`        | Name of the dataset                              |
| `images`       | Array of image objects (initially empty)         |
| `image_names`  | List of image filenames                          |
| `input_folder` | Relative or absolute path to the image directory |

---

## 💡 Usage

### Run the Main Script

```bash
./manage.sh run <json file path>
```

Example:

```bash
./manage.sh run datasets/sample.json
```

### Run Unit Tests

```bash
./manage.sh test
```

### Check PEP8 Compliance

```bash
./manage.sh style <python file path>
```

Example:

```bash
./manage.sh style src/main.py
```

### Clear Build Files

```bash
./manage.sh clear
```

---

## 🧠 Architecture

The codebase uses the **Template Design Pattern** to separate image quality assessment logic from dataset loading implementations.

This design allows developers to:

* Add new dataset loaders easily
* Reuse the evaluation pipeline
* Extend the framework for additional IQA methods

---

## 🤝 Contributing

Contributions are welcome.

If you find a bug or want to suggest improvements:

1. Open an issue
2. Submit a pull request
3. Follow existing code style conventions

Please ensure all tests pass before submitting changes.

---

## 📄 License

This project is licensed under the MIT License.
