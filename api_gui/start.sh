#!/usr/bin/env bash
python3 fill_dbs.py /api_gui
uwsgi --ini uwsgi.ini