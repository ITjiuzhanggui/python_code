#!/bin/sh
set -e

swupd bundle-add wget linux-tools c-basic
GOBIN=$GOPATH/bin
TESTDIR=$GOPATH/src/golang.org
mkdir -p $TESTDIR && cd $TESTDIR
wget http://www.phoronix-test-suite.com/benchmark-files/golang-benchmarks-121017.tar.gz
tar zxf golang-benchmarks-121017.tar.gz
mv go-benchmark-04122017/x x
go install golang.org/x/benchmarks/...

cd $GOBIN
test_cmd=`ls .`

for cmd in $test_cmd; do
    ./$cmd
done

