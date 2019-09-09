#!/bin/bash

python /data/protocol.py /data/conf.json /data/policy.json
python /app/post-data.py
