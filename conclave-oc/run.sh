#!/bin/bash

python3.5 /app/decode.py
python3.5 /app/pull-data.py
python3.5 /app/protocol.py --conf /app/conf.json
python3.5 /app/post-data.py
