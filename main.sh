#!/bin/sh

cd scripts

if [ ! -f feeds.db ]; then
    python3 databaseCreation.py
fi

python3 -m flask --app frontend run