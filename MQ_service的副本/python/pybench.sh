#!/bin/sh
set -e

apt-get update 
apt-get install -y --no-install-recommends
apt-get install wget
wget http://www.phoronix-test-suite.com/benchmark-files/pybench-2018-02-16.tar.gz
tar -xvf pybench-2018-02-16.tar.gz
cd pybench-2018-02-16
python3 pybench.py
