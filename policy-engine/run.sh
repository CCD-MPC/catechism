#!/bin/bash

python /app/decode.py
python /app/pull_policy.py
python /app/protocol_policy.py /app/in-conf.json /app/policy.json
