#!/usr/bin/env bash


set -e
.  ~/.env/tdd/bin/activate 
cd ./src && python manage.py test lists && python manage.py test functional_test
