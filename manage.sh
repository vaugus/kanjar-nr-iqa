#!/bin/bash

case $1 in
    clear)
        rm -rf */__pycache__ 
        rm -f -- output/*.txt ;;
    run)
        python src/main $2 ;;
    style)
        pycodestyle --show-source --show-pep8 $2 ;;
    test)
        python -m unittest ;;
    *)
        echo "Unsupported operation."
        echo
esac