#!/usr/bin/env bash
# Copyright (C) 2018 Intel Corporation
# SPDX-License-Identifier: Apache-2.0


LOG_DOMAIN=redis 

. ./common.sh

section "redis unit test"

sudo docker network ls | grep redis-network
if [ $? -ne 0 ]; then
    sudo docker network create redis-network
fi

set -e

info "Test docker hub official image first"
sudo docker run --name some-redis --network redis-network -d --rm redis
sleep 1
sudo docker run --network redis-network --rm redis redis-benchmark -h some-redis
sleep 1
sudo docker stop some-redis

info "Test clear docker image"
sudo docker run --name clr-redis --network redis-network -d --rm clearlinux/redis redis-server --protected-mode no
sleep 1
sudo docker run --network redis-network --rm clearlinux/redis redis-benchmark -h clr-redis
sleep 1
sudo docker stop clr-redis

