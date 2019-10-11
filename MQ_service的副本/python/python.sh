#!/usr/bin/env bash
# Copyright (C) 2018 Intel Corporation
# SPDX-License-Identifier: Apache-2.0


LOG_DOMAIN=python

. ./common.sh

section "python unit test"

info "Test docker hub official image first"
sudo docker run --rm --cap-add SYS_ADMIN --env http_proxy=$http_proxy --env https_proxy=$https_proxy -v $PWD/python:/test --entrypoint "/test/pybench.sh" python

info "Test clear docker image"
sudo docker run --rm --cap-add SYS_ADMIN --env http_proxy=$http_proxy --env https_proxy=$https_proxy -v $PWD/python:/test --entrypoint "/test/clear-pybench.sh" clearlinux/python

