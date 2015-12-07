#!/bin/bash

cd $( dirname "${BASH_SOURCE[0]}" )
echo $USER
source /usr/local/bin/virtualenvwrapper.sh

workon opentrain2

python manage.py "$@"




