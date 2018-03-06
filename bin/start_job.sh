#!/usr/bin/env bash

BIN_PATH=$(cd `dirname $0`; pwd)
python -u "$BIN_PATH/hive_email_job.py " $@
