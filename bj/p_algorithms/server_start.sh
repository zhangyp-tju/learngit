#!bin/bash

# function : run server ---- Usage:sh ./server_start.sh
# Author : zyp
# Written : 2015/06/15
# Rewriten : 2015/06/15
# Copyright: sogou

printf "running server....\n"
# run server on using the abstract path
python2.6 /search/zyp/subtopic_platform/manage.py runserver 0.0.0.0:8899

printf "run successfully....\n"
