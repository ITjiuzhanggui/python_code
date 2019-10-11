#!/usr/bin/env bash
# Copyright (C) 2018 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

set -e

LOG_DOMAIN=update
TEST_UNITS=$1

. ./common.sh

section "Updating the container images: ${TEST_UNITS}"

sudo docker pull clearlinux

for file in ${TEST_UNITS}; do
    sudo docker pull $file
    sudo docker pull clearlinux/$file
done


