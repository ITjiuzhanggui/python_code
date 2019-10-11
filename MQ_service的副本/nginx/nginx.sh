#!/usr/bin/env bash
# Copyright (C) 2018 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

LOG_DOMAIN=nginx

. ./common.sh

section "nginx unit test"

# Install test tools apache bench
sudo swupd bundle-list | grep httpd
if [ $? -ne 0 ]; then
        sudo swupd bundle-add httpd
fi

set -e

info "Test docker hub official image first"
sudo docker run --name nginx-server --rm -dit -p 8080:80 nginx
sleep 1
ab -n 100000 -c 50 -k http://localhost:8080/
sleep 1
sudo docker stop nginx-server

info "Test clear docker image"
sudo docker run --name clr-nginx-server --rm -dit -p 8088:80 clearlinux/nginx
sleep 1
ab -n 100000 -c 50 -k http://localhost:8088/
sleep 1
sudo docker stop clr-nginx-server

