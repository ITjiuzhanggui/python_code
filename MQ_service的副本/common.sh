#!/usr/bin/env bash
# Copyright (C) 2018 Intel Corporation
# SPDX-License-Identifier: Apache-2.0


# LOG_DOMAIN = Domain name to be printed in the beginning of each log line
# LOG_INDENT = Indentation level to be applied on the log message after 'domain'
log_line() {
    # ${1} - log message
    # ${2} - extra indentation

    local indent=${1:+$(( (${LOG_INDENT:-0} + ${2:-0}) * 4 ))}
    printf "${LOG_DOMAIN:+"[${LOG_DOMAIN}] "}%${indent}s%s\\n" "" "${1}"
}

log() {
    # ${1} - log title (or message for single line logs)
    # ${2} - log message (optional)
    # ${3} - extra indentation (optional, requires ${2})

    if (( $# < 2 )); then
        log_line "${1}"
    else
        log_line "${1}:" "${3}"
        log_line "${2}" $((${3:-0} + 1))
    fi
}


section() {
    log_line
    log_line "== ${1} =="
}

error() {
    log "[ERROR] ${1}" ${2:+"${2}"} "${3}"
}

info() {
    log "[INFO] ${1}" ${2:+"${2}"} "${3}"
}

warn() {
    log "[WARN] ${1}" ${2:+"${2}"} "${3}"
}

