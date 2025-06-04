#!/bin/bash

cd /path/to/CommitFarm

DELAY=$(( RANDOM % 14400 ))
echo "Sleeping for $DELAY seconds before running script..."
sleep $DELAY

/path/to/CommitFarm/venv/bin/python app.py
