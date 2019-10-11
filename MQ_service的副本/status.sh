#!/usr/bin/env bash
# Copyright (C) 2018 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

set -e

LOG_DOMAIN=status
TEST_UNITS=$1

. ./common.sh

section "Get general information of container images"

for file in ${TEST_UNITS}; do
    sudo docker images $file
    sudo docker images clearlinux/$file
    python extract_clr_layer_size.py -f $file 
    sudo docker run --rm clearlinux/$file swupd info
    echo ""
    echo ""
done


