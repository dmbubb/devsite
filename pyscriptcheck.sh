#!/usr/bin/env bash

FILEPATH=$(pwd)
find ${FILEPATH} -iname "*.pyc" -exec rm {} \;
python -m compileall -q ${FILEPATH}
find ${FILEPATH} -iname "*.pyc" -exec rm {} \;
python3 -m compileall -q ${FILEPATH}
find ${FILEPATH} -iname "*.pyc" -exec rm {} \;
