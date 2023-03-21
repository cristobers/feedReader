#!/bin/sh

cd scripts

if [ ! -f feeds.db ]; then
    python3 databaseCreation.py
fi

if [ ! -f sortby ]; then
    touch sortby && echo "All" > sortby
fi

python3 -m flask --app frontend run
