#!/bin/bash
touch __init__.py
time python $(which pylint) --rcfile=.pylintrc $(pwd)
# save exit_code for check at end
exit_code=$?
rm __init__.py

if [[ exit_code -ne 0 ]] ; then
    exit $exit_code
fi