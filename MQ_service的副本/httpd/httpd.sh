#!/usr/bin/env bash
# Copyright (C) 2018 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

LOG_DOMAIN=httpd 

. ./common.sh

section "httpd unit test"

# Install test tools apache bench
sudo swupd bundle-list | grep httpd
if [ $? -ne 0 ]; then
	sudo swupd bundle-add httpd
fi

set -e

info "Test docker hub official image first"
sudo docker run --name httpd-server --rm -dit -p 8080:80 httpd
sleep 1
ab -n 100000 -c 50 -k http://localhost:8080/
sleep 1
sudo docker stop httpd-server

info "Test clear docker image"
sudo docker run --name clr-httpd-server --rm -dit -p 8088:80 clearlinux/httpd
sleep 1
ab -n 100000 -c 50 -k http://localhost:8088/
sleep 1
sudo docker stop clr-httpd-server

