#!/bin/sh
set -e

swupd bundle-add wget unzip
wget http://phoronix-test-suite.com/benchmark-files/phpbench-081-patched1.zip
unzip phpbench-081-patched1.zip  
cd phpbench-0.8.1-patched1
php phpbench.php
