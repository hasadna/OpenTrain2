#!/bin/bash

cd $( dirname "${BASH_SOURCE[0]}" )
echo $USER
export VIRTUALENVWRAPPER_PYTHON=$(which python3)
source /usr/local/bin/virtualenvwrapper.sh

workon ot2

python manage.py "$@"




