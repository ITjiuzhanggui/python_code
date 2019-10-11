#!/bin/sh
set -e

swupd bundle-add wget
wget http://www.phoronix-test-suite.com/benchmark-files/pybench-2018-02-16.tar.gz
tar -xvf pybench-2018-02-16.tar.gz
cd pybench-2018-02-16
python3 pybench.py
