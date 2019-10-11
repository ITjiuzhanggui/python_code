#!/bin/sh
set -e

swupd bundle-add wget unzip
wget http://phoronix-test-suite.com/benchmark-files/benchmark-octane-20181001.zip
unzip benchmark-octane-20181001.zip
cd benchmark-octane-master
node run.js
