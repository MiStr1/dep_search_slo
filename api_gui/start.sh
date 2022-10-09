#!/usr/bin/env bash
python3 fill_dbs.py /corpus/
python3 start_cached_queries.py &
uwsgi --ini uwsgi.ini
