#!/usr/bin/env bash

set -e

.  ~/.env/tdd/bin/activate 

cd ./src && python manage.py test lists 
python ./src/manage.py test functional_tests 
coverage ./src/manage.py run test lists -v 2
