#!/bin/bash
cat $1 | python2.6 updateAverageReadnum.py  > $2
