#!/bin/bash

python /app/decode.py
python /app/pull-data.py
python /app/protocol.py --conf /app/conf.json
python /app/post-data.py
