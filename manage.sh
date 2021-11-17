#!/bin/bash

case $1 in
    clear)
        rm -rf */__pycache__ 
        rm -f -- output/*.txt ;;
    style)
        pycodestyle --show-source --show-pep8 $2 ;;
    test)
        python -m unittest ;;
    run)
        python main.py $2 ;;
    *)
        echo "Unsupported operation."
        echo
esac