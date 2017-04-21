#!/usr/bin/env bash

cd ./src && python manage.py test lists && python manage.py test functional_test
