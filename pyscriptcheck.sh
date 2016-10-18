#!/usr/bin/env bash

FILEPATH=$(pwd)
find ${FILEPATH} -iname "*.pyc" -exec rm {} \;
python -m compileall -q ${FILEPATH}
compile_result =  $?
find ${FILEPATH} -iname "*.pyc" -exec rm {} \;
exit ${compile_result}
