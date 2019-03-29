#!/usr/bin/env bash
python3 wait_for_web.py
python3 wait_for_rabbit.py

celery -A Project_1 worker -B -l info