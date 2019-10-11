#!/usr/bin/env bash
# Copyright (C) 2018 Intel Corporation
# SPDX-License-Identifier: Apache-2.0


LOG_DOMAIN=golang

. ./common.sh

section "golang unit test"

info "Test docker hub official image first"
sudo docker run --rm --cap-add SYS_ADMIN --env http_proxy=$http_proxy --env https_proxy=$https_proxy -v $PWD/golang:/test --entrypoint "/test/gobench.sh" golang

info "Test clear docker image"
sudo docker run --rm --cap-add SYS_ADMIN --env http_proxy=$http_proxy --env https_proxy=$https_proxy -v $PWD/golang:/test --entrypoint "/test/clear-gobench.sh" clearlinux/golang

