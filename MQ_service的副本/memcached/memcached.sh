#!/usr/bin/env bash
# Copyright (C) 2018 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

LOG_DOMAIN=memcached 

. ./common.sh

section "memcached unit test"

sudo docker network ls | grep memcached-network
if [ $? -ne 0 ]; then
    sudo docker network create memcached-network
fi

set -e

info "Test docker hub official image first"
sudo docker run --network memcached-network --name memcached-server -d --rm memcached
sleep 5
sudo docker run --rm --network memcached-network redislabs/memtier_benchmark ./memtier_benchmark --server=memcached-server -p 11211 -P memcache_text
sleep 1
sudo docker stop memcached-server

info "Test clear docker image"
sudo docker run --network memcached-network --name cl-memcached-server -d --rm clearlinux/memcached
sleep 5
sudo docker run --rm --network memcached-network redislabs/memtier_benchmark ./memtier_benchmark --server=cl-memcached-server -p 11211 -P memcache_text
sleep 1
sudo docker stop cl-memcached-server
